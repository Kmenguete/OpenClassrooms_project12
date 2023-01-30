from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contract
from .serializers import ContractSerializer
from .permissions import IsSalesContact


class ContractViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSalesContact]
    http_method_names = ["get", "post", "put"]
    serializer_class = ContractSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['client', 'date_created', 'amount', 'payment_due']
    search_fields = ['client', 'date_created', 'amount', 'payment_due']
    ordering_fields = ['id', 'date_created', 'amount', 'payment_due']
    ordering = ['id']

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(sales_contact=user)

    def create(self, request, *args, **kwargs):
        if request.user.role != "Sales Contact":
            raise PermissionDenied
        else:
            request.POST._mutable = True
            request.data["sales_contact"] = request.user.pk
            request.POST._mutable = False
        return super(ContractViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.role != "Sales Contact":
            raise PermissionDenied
        else:
            serializer.save(sales_contact=self.request.user)
