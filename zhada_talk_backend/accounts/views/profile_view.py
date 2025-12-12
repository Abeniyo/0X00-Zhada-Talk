from rest_framework import generics, permissions
from accounts.models import Profile
from accounts.serializers.profile_serializer import (
    ProfileSerializer,
    ProfileUpdateSerializer,
)


class ProfileDetailView(generics.RetrieveAPIView):
    """GET /profile/me/ — Get logged-in user's profile"""

    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(generics.UpdateAPIView):
    """PATCH /profile/me/update/ — Update profile info"""

    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
