from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers import (
    UserSerializer,
    SessionLoginSerializer,
)

from utils.permissions import IsStaff


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer
    permission_classes = [IsStaff]


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class SessionLoginView(APIView):
    serializer_class = SessionLoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return Response({"message": "Login successful."})
                else:
                    return Response(
                        {"message": "User account is not active."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"message": "Invalid credentials."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionLogoutView(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response(
            {"message": "Logged out successfully."}, status=status.HTTP_200_OK
        )
