# accounts/urls.py

from django.urls import path, include
from accounts.views.user_view import UserDetailView, UserUpdateView
from accounts.views.profile_view import ProfileDetailView, ProfileUpdateView
from accounts.views.auth_view import LoginAPIView, LogoutAPIView, CustomRegisterView, PasswordChangeView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # --------------------------
    # USER ENDPOINTS
    # --------------------------
    path("users/me/", UserDetailView.as_view(), name="user-detail"),
    path("users/me/update/", UserUpdateView.as_view(), name="user-update"),

    # --------------------------
    # PROFILE ENDPOINTS
    # --------------------------
    path("profile/me/", ProfileDetailView.as_view(), name="profile-detail"),
    path("profile/me/update/", ProfileUpdateView.as_view(), name="profile-update"),

    # --------------------------
    # AUTHENTICATION ENDPOINTS
    # --------------------------
    path("register/", CustomRegisterView.as_view(), name="auth-register"),
    path("login/", LoginAPIView.as_view(), name="auth-login"),
    path("logout/", LogoutAPIView.as_view(), name="auth-logout"),
    path("password/change/", PasswordChangeView.as_view(), name="auth-password-change"),

    # JWT refresh token
    path("token/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),

    # dj-rest-auth built-in endpoints for password reset, email verification
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
