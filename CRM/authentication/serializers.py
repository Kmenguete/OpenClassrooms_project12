from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserSerializer(ModelSerializer):
    model = CustomUser
    fields = ["id", "email", "first_name",
              "last_name", "role",
              "is_staff", "is_active", "date_joined"]
