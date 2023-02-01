from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .permissions import IsSalesContact, IsSupportContact, PastDate
from .serializers import EventSerializer, SupportEventSerializer
from client.models import Client


class EventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSalesContact, PastDate]
    http_method_names = ["get", "post"]
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
            user = self.request.user
            events = get_event_for_sales_contact(user)
            return events
        else:
            return Event.objects.filter(support_contact=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.role != "Sales Contact":
            raise PermissionDenied
        else:
            return super(EventViewSet, self).create(request, *args, **kwargs)


class SupportEventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSupportContact, PastDate]
    http_method_names = ["get", "put"]
    serializer_class = SupportEventSerializer
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
            user = self.request.user
            events = get_event_for_sales_contact(user)
            return events
        else:
            return Event.objects.filter(support_contact=self.request.user)

    def update(self, request, *args, **kwargs):
        if request.user.role != "Support Contact":
            raise PermissionDenied
        else:
            return super(SupportEventViewSet, self).update(request, *args, **kwargs)


def get_event_for_sales_contact(user):
    clients = Client.objects.filter(sales_contact=user)
    events_to_get = [clients]
    for client in events_to_get:
        events = Event.objects.filter(client__id__in=client)
        return events
