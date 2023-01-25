from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put"]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(support_contact=user)

    def create(self, request, *args, **kwargs):
        if request.user.role != "Sales Contact":
            raise PermissionDenied
        else:
            return super(EventViewSet, self).create(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(sales_contact=self.request.user)
