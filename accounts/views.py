from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . serializers import UserCreationSerializer, UserDetailsSerializer
from .models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Auth"}, status=status.HTTP_200_OK)


class UserRegisterAPIView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer

    @swagger_auto_schema(operation_summary="Create A User Account")
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)