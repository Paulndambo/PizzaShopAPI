from ast import Or
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . serializers import OrderCreationSerializer, OrderDetailSerializer, OrderStatusUpdateSerializer
from . models import Order
from accounts.models import User
from orders import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
# Create your views here.
class HelloOrdersView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Orders"}, status=status.HTTP_200_OK)


class OrderListCreateAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()

    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        customer = request.user

        if serializer.is_valid():
            serializer.save(customer=customer)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderDetailSerializer

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(data=data, instance=order)
        customer = request.user
        if serializer.is_valid():
            serializer.save(customer=customer)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(data=data, instance=order)
        if serializer.is_valid():
            order.delete()
            return Response({"success": "Order Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"failed": "Order could not be deleted"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrderStatusAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderStatusUpdateSerializer

    def put(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(data=data, instance=order)
        order_status = data['order_status']
        if serializer.is_valid():
            serializer.save(order_status=order_status)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrdersAPIView(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)

        orders = Order.objects.filter(customer=user)
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrderDetailAPIView(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer

    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.filter(customer=user).filter(pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
