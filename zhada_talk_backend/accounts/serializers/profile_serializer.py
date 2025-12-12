from rest_framework import serializers
from accounts.models import Profile
from .user_serializer import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    """Return full profile data including nested user info"""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "bio",
            "profile_image",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """User can update only bio + profile image"""

    class Meta:
        model = Profile
        fields = ["bio", "profile_image"]
