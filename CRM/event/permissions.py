from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS
from datetime import datetime
import pytz


class IsSalesContact(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.support_contact != request.user


class IsSupportContact(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.support_contact == request.user


class PastDate(BasePermission):

    def has_object_permission(self, request, view, obj):
        if datetime.strptime(str(obj.event_date), "%Y-%m-%d %H:%M:%S%f%z") < datetime.now().replace(tzinfo=pytz.UTC):
            raise PermissionDenied("An event cannot take place on a past date.")
