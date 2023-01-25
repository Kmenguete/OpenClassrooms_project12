from django.contrib.auth.views import LogoutView
from rest_framework import viewsets, filters
from .authentication import MyAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import CustomUser
from .serializers import UserSerializer
from CRM import settings


class UserViewSet(ReadOnlyModelViewSet):

    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['role', 'email',
                     'first_name', 'last_name', 'date_joined']

    def get_queryset(self):
        return CustomUser.objects.all()


class LoginViewSet(viewsets.ViewSet):
    authentication_classes = [MyAuthentication]


class SignOutView(LogoutView):

    def get_success_url(self):
        return settings.LOGOUT_REDIRECT_URL
