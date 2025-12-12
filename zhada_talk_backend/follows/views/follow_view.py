from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models.follow import Follow
from ..serializers.follow_serializer import FollowSerializer, FollowerListSerializer, FollowingListSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def follow(self, request):
        user_to_follow_id = request.data.get('user_id')
        if not user_to_follow_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.id) == str(user_to_follow_id):
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            target_user = User.objects.get(id=user_to_follow_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        follow, created = Follow.objects.get_or_create(follower=request.user, following=target_user)
        if not created:
            return Response({"status": "Already following"}, status=status.HTTP_200_OK)
        serializer = FollowSerializer(follow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def unfollow(self, request):
        user_to_unfollow_id = request.data.get('user_id')
        try:
            target_user = User.objects.get(id=user_to_unfollow_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        deleted, _ = Follow.objects.filter(follower=request.user, following=target_user).delete()
        if deleted:
            return Response({"status": "Unfollowed successfully"})
        return Response({"status": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def followers(self, request):
        followers = Follow.objects.filter(following=request.user)
        serializer = FollowerListSerializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def following(self, request):
        following = Follow.objects.filter(follower=request.user)
        serializer = FollowingListSerializer(following, many=True)
        return Response(serializer.data)
