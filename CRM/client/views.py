from rest_framework.viewsets import ModelViewSet

from CRM.client.models import Client
from CRM.client.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()
