from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="user-register"),
    path("profile/", views.UserProfileView.as_view(), name="user-profile"),
    path("profile/update-login-credentials/", views.UserLoginAndSecurityView.as_view(), name="user-update-login-credentials"),
    path("profile/<int:pk>/update-profile/", views.UserProfileUpdateView.as_view(), name="user-update-profile"),
]