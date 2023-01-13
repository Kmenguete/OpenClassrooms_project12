from rest_framework.viewsets import ModelViewSet

from CRM.client.models import Client
from CRM.client.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put"]
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["sales_contact"] = request.user.pk
        request.POST._mutable = False
        return super(ClientViewSet, self).create(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(sales_contact=self.request.user)
