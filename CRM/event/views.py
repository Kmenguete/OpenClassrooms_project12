from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer
from .permissions import IsSupportContact


class EventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSupportContact]
    http_method_names = ["get", "post", "put"]
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['client', 'date_created',
                        'attendees', 'event_date']
    search_fields = ['client', 'date_created',
                     'attendees', 'event_date']
    ordering_fields = ['id', 'client', 'date_created',
                       'attendees', 'event_date']
    ordering = ['id']

    def get_queryset(self):
        if self.request.user.role == "Sales Contact":
            return Event.objects.all()
        else:
            return Event.objects.filter(support_contact=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.role != "Sales Contact":
            raise PermissionDenied
        else:
            return super(EventViewSet, self).create(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(support_contact=self.request.user)
