from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
