from rest_framework import generics, permissions, status, throttling
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.registration.views import RegisterView
from accounts.serializers.auth_serializer import (
    LoginSerializer,
    CustomRegisterSerializer,
    PasswordChangeSerializer
)
from django.contrib.auth import get_user_model

User = get_user_model()


# --------------------------
# Throttles
# --------------------------
class LoginThrottle(throttling.AnonRateThrottle):
    scope = "login"


class RegisterThrottle(throttling.AnonRateThrottle):
    scope = "register"


class ResetThrottle(throttling.AnonRateThrottle):
    scope = "reset"


# --------------------------
# Login (JWT)
# --------------------------
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    throttle_classes = [LoginThrottle]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        # JWT only
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=200)


# --------------------------
# Logout (invalidate session)
# --------------------------
class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        user.is_online = False
        user.save(update_fields=["is_online"])

        # Invalidate Django session
        logout(request)

        return Response({"detail": "Logged out successfully."}, status=200)


# --------------------------
# Registration
# --------------------------
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    throttle_classes = [RegisterThrottle]
    permission_classes = [permissions.AllowAny]


# --------------------------
# Password Change
# --------------------------
class PasswordChangeView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old = serializer.validated_data["old_password"]
        new = serializer.validated_data["new_password"]

        if not request.user.check_password(old):
            return Response({"detail": "Old password incorrect."}, status=400)

        request.user.set_password(new)
        request.user.save()

        return Response({"detail": "Password updated successfully."})
