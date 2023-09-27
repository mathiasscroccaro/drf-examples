from django.contrib.auth import (
    get_user_model,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    password = serializers.CharField(
        max_length=250, min_length=5, allow_blank=True, write_only=True
    )

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name", "is_staff"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}
        extra_kwargs = {"is_staff": {"read_only": True}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class SessionLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
