from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Contract
from .serializers import ContractSerializer


class ContractViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put"]
    serializer_class = ContractSerializer

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(sales_contact=user)

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["sales_contact"] = request.user.pk
        request.POST._mutable = False
        return super(ContractViewSet, self).create(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(sales_contact=self.request.user)
