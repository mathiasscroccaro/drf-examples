from django.contrib import admin
from django.urls import path, include


from django.urls import re_path
from django.contrib.staticfiles import views


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^static/(?P<path>.*)$", views.serve),
    path("user/", include("user.urls")),
]
