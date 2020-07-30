from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user.role in ['admin', 'moderator']:
            return True

        return obj.author == request.user
