from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()


class LoginAPIView(APIView):

    def get(self):
        user = self.request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
