from rest_framework import authentication, exceptions

from .models import CustomUser


class MyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.META.get('email')
        password = request.META.get('password')
        user = CustomUser.objects.get(email=email)
        if not email or not password:
            raise exceptions.AuthenticationFailed('No credentials provided.')
        elif email or password is None:
            raise exceptions.AuthenticationFailed('Invalid username/password.')
        elif not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user, None)
