from rest_framework import authentication
from rest_framework import exceptions

from CRM.authentication.models import CustomUser


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.META.get('email')  # get the email request header
        if not email:  # no email passed in request headers
            return None  # authentication did not succeed

        try:
            user = CustomUser.objects.get(email=email)  # get the user
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')  # raise exception if user does not exist

        return user, None  # authentication successful
