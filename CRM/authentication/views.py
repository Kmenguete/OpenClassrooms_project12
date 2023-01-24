from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from rest_framework import viewsets
from .authentication import MyAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()


class LoginViewSet(viewsets.ViewSet):
    authentication_classes = [MyAuthentication]


class LogoutViewSet(viewsets.ViewSet, LogoutView):

    def get_redirect_url(self):
        return redirect(settings.LOGOUT_REDIRECT_URL)
