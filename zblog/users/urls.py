from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="user-register"),
    path("login/", auth_views.LoginView.as_view(), name="user-login"),
    path("logout/", auth_views.LogoutView.as_view(), name="user-logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),

    path("profile/", views.UserProfileView.as_view(), name="user-profile"),
    path("profile/update-login-credentials/", views.UserLoginAndSecurityView.as_view(), name="user-update-login-credentials"),
    path("profile/update-login-credentials/pswd-change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("profile/update-login-credentials/pswd-change/done/",
         auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path("profile/update-profile/", views.UserProfileUpdateView.as_view(), name="user-update-profile"),
]