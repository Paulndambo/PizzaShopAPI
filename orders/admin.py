from django.contrib import admin
from . models import Order
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "size", "quantity", "order_status", "created_at", "updated_at"]
    list_filter = ["size", "created_at", "order_status"]