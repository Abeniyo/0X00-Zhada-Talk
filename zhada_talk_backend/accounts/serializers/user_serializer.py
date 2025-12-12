from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Public user data (safe fields only)"""

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "full_name",
            "gender",
            "age",
            "is_verified",
            "is_online",
        ]
        read_only_fields = ["id", "is_verified", "is_online"]

    def get_full_name(self, user):
        return f"{user.first_name} {user.last_name}".strip()


class UserUpdateSerializer(serializers.ModelSerializer):
    """Allow users to update their own fields"""

    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "age",
        ]
