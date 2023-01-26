from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSalesContact(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

    def has_permission(self, request, view):
        if view.action not in ("put",):
            return True
        elif view.action in ("post",):
            return True


class IsSupportContact(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.support_contact == request.user

    def has_permission(self, request, view):
        if view.action not in ("post",):
            return True
        elif view.action in ("put",):
            return True
