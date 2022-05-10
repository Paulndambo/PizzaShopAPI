from . models import Order
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class OrderCreationSerializer(ModelSerializer):
    size = serializers.CharField(max_length=200)
    order_status = serializers.HiddenField(default="pending")
    quantity = serializers.IntegerField(default=0)

    class Meta:
        model = Order
        fields = ["id", "size", "order_status", "quantity"]

class OrderDetailSerializer(ModelSerializer):
    #size = serializers.CharField(max_length=200)
    #quantity = serializers.IntegerField(default=0)
    #customer = serializers.MethodField(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "size", "order_status", "quantity", "created_at", "updated_at"]

class OrderStatusUpdateSerializer(ModelSerializer):
    order_status = serializers.HiddenField(default="pending")
    class Meta:
        model = Order
        fields = ['order_status']

