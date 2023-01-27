from rest_framework import permissions


class IsStaffOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') demektir.
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
