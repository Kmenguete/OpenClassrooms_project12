from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "put"]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def perform_update(self, serializer):
        serializer.save(sales_contact=self.request.user)
