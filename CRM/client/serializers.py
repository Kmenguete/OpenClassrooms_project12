from rest_framework.serializers import ModelSerializer

from .models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name',
                  'email', 'phone', 'mobile', 'company_name',
                  'date_created', 'date_updated', 'sales_contact']
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        user = self.context["request"].user
        client = Client.objects.create(**validated_data, sales_contact=user)

        return client
