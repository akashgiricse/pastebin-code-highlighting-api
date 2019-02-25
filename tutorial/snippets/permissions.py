from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission to only allow owners of an object to delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permission is allowed to any request object
        # so we will always allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
