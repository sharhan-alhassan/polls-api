

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    '''
    Read-only for all requests but for any write
    requests, such as edit or delete, the author must be the same as the current logged-
    in user.
    SAFE_METHODS -- these are GET, OPTIONS, HEAD which is read only
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post. Basically object-level permission
        return obj.author == request.user
