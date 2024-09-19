
from rest_framework.permissions import BasePermission

class IsOwnerAndAuthenticated(BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Object-level permission to only allow the owner of the article to access it.
        Assumes that the  model has an `user` attribute.
        """
        # Check if the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Allow access only if the authenticated user is the owner of the article
        return obj.user == request.user
