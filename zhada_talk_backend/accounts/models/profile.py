from django.db import models
from django.conf import settings
from django.utils import timezone

def profile_image_upload_to(instance, filename):
    return f"profile_images/{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to=profile_image_upload_to,
        default='defaults/default_profile.png',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.first_name} {self.user.last_name}"
