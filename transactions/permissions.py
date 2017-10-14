from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Object-level permissions to only allow owners of a transactions to handle it
    """
    message = "You're now allowed to handle this since it's not belongs to you"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user