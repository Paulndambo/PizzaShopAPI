from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Order(models.Model):
    PIZZA_CHOICES = (
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
        ("extra_large", "Extra Large"),
    )
    ORDER_STATUS = (
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=200, choices=PIZZA_CHOICES, default=PIZZA_CHOICES[0][0])
    order_status = models.CharField(max_length=200, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"<Order {self.size} by {self.customer.username}"

