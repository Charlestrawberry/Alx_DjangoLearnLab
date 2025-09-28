from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins (staff users)
    to edit objects, while anyone can read.
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # For unsafe methods (POST, PUT, DELETE),
        # only allow if user is admin
        return request.user and request.user.is_staff
