from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSupportContact(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method in ('POST',):
            return True
        else:
            return obj.support_contact == request.user
