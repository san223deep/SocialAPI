from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from .serializers import *
from social.models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q


class data_update(APIView):

    def post(self, request):
        serializer = DataUpdateSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():

            user_id = request.data['user_id']
            if User.objects.filter(user_id=user_id):
                user = User.objects.get(user_id=user_id)
            else:
                user = User()
                user.user_id = user_id
            user.username = request.data['user_id']
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.email = request.data['email']
            user.balance = request.data['balance']
            user.device_id = request.data['device_id']
            user.platform = request.data['platform']
            user.user_id = request.data['user_id']
            user.save()
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
