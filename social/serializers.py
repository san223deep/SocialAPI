from .models import User
from rest_framework import serializers


class DataUpdateSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_id', 'balance', 'device_id', 'platform')





