from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Contract
from client.models import Client


class CustomForeignKey(PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context["request"].user
        return Client.objects.filter(sales_contact=user)


class ContractSerializer(ModelSerializer):
    client = CustomForeignKey()

    class Meta:
        model = Contract
        fields = [
            "id",
            "sales_contact",
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payment_due",
        ]

        read_only_fields = ["sales_contact"]

        def create(self, validated_data):
            user = self.context["request"].user
            contract = Contract.objects.create(**validated_data, sales_contact=user)
            return contract
