from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Event
from client.models import Client


class CustomForeignKey(PrimaryKeyRelatedField):

    def get_queryset(self):
        user = self.context["request"].user
        return Client.objects.filter(sales_contact=user)


class EventSerializer(ModelSerializer):
    client = CustomForeignKey()

    class Meta:
        model = Event
        fields = ["id", "client",
                  "date_created", "date_updated",
                  "support_contact", "event_status",
                  "attendees", "event_date", "notes"]
