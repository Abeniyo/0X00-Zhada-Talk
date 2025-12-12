from rest_framework import serializers
from ..models.follow import Follow
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowSerializer(serializers.ModelSerializer):
    follower_email = serializers.ReadOnlyField(source='follower.email')
    following_email = serializers.ReadOnlyField(source='following.email')

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'follower_email', 'following_email', 'created_at']

class FollowerListSerializer(serializers.ModelSerializer):
    follower_email = serializers.ReadOnlyField(source='follower.email')

    class Meta:
        model = Follow
        fields = ['id', 'follower_email', 'created_at']

class FollowingListSerializer(serializers.ModelSerializer):
    following_email = serializers.ReadOnlyField(source='following.email')

    class Meta:
        model = Follow
        fields = ['id', 'following_email', 'created_at']
