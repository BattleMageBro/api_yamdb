from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class IsModerator(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if obj.author != request.user:
            if request.user.role == 'moderator':
                return True
            return False

        return True


