from rest_framework import authentication, exceptions

from .models import CustomUser


class MyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.META.get('email')
        password = request.META.get('password')
        if not email and password:
            return None
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return user, None
