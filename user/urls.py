from django.urls import path

from user import views


app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("me/", views.ManageUserView.as_view(), name="me"),
    path("session-login/", views.SessionLoginView.as_view(), name="session-login"),
    path("session-logout/", views.SessionLogoutView.as_view(), name="session-logout"),
]
