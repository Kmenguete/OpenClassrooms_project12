from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer

    def get_object(self):
        return CustomUser.objects.filter(id=self.request.user.id)
