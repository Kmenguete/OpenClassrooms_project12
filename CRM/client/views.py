from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client
from .permissions import IsSalesContact
from .serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSalesContact]
    http_method_names = ["get", "post", "put"]
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'last_name',
                        'email', 'company_name', 'date_created']
    search_fields = ['^first_name', '^last_name',
                     '^email', '^company_name', 'date_created']
    ordering_fields = ['id', 'first_name', 'last_name',
                       'email', 'company_name', 'date_created']
    ordering = ['id']

    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(sales_contact=user)

    def create(self, request, *args, **kwargs):
        if request.user.role != "Sales Contact":
            raise PermissionDenied
        else:
            request.POST._mutable = True
            request.data["sales_contact"] = request.user.pk
            request.POST._mutable = False
        return super(ClientViewSet, self).create(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(sales_contact=self.request.user)
