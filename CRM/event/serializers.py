from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Event
from client.models import Client

from authentication.models import CustomUser

from contract.models import Contract


class ClientForeignKey(PrimaryKeyRelatedField):

    def get_queryset(self):
        user = self.context["request"].user
        return Client.objects.filter(sales_contact=user)


class ContractForeignKey(PrimaryKeyRelatedField):

    def get_queryset(self):
        user = self.context["request"].user
        return Contract.objects.filter(sales_contact=user)


class SupportContactForeignKey(PrimaryKeyRelatedField):

    def get_queryset(self):
        return CustomUser.objects.filter(role="Support Contact")


class EventSerializer(ModelSerializer):
    client = ClientForeignKey()
    event_status = ContractForeignKey()
    support_contact = SupportContactForeignKey()

    class Meta:
        model = Event
        fields = ["id", "client",
                  "date_created", "date_updated",
                  "support_contact", "event_status",
                  "attendees", "event_date", "notes"]


class SupportEventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ["id", "client",
                  "date_created", "date_updated",
                  "support_contact", "event_status",
                  "attendees", "event_date", "notes"]
        read_only_fields = ["client", "support_contact", "event_status"]
