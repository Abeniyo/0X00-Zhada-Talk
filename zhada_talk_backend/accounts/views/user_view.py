from rest_framework import generics, permissions
from accounts.models import User
from accounts.serializers.user_serializer import (
    UserSerializer,
    UserUpdateSerializer,
)


class UserDetailView(generics.RetrieveAPIView):
    """GET /users/me/ — Get current authenticated user"""

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserUpdateView(generics.UpdateAPIView):
    """PATCH /users/me/update/ — Update user information"""

    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
