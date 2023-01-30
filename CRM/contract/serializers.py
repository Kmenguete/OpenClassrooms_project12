from rest_framework.serializers import ModelSerializer

from .models import Contract
from client.models import Client


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ["id", "sales_contact",
                  "client", "date_created",
                  "date_updated", "status",
                  "amount", "payment_due"]

        read_only_fields = ['sales_contact']

        def create(self, validated_data):
            user = self.context["request"].user
            contract = Contract.objects.create(**validated_data, sales_contact=user)
            clients = Client.object.filter(**validated_data, sales_contact=user)

            return contract, clients
