from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.follow_view import FollowViewSet

router = DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = router.urls
