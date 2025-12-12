from rest_framework.permissions import BasePermission

class RoleRequired(BasePermission):
    required_groups = []

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name__in=self.required_groups).exists()
