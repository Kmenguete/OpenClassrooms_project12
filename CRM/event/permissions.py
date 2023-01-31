from rest_framework.permissions import BasePermission


class IsSupportContact(BasePermission):

    def has_permission(self, request, view):
        if view.action not in ("post",):
            return True
        elif view.action in ("put",):
            return True
