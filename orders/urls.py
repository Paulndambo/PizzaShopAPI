from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.HelloOrdersView.as_view(), name="hello-orders"),
    path("list-create-orders/", views.OrderListCreateAPIView.as_view(), name="list-create-orders"),
    path("order/<int:order_id>/", views.OrderDetailAPIView.as_view(), name="order"),
    path("update-order-status/<int:order_id>/", views.UpdateOrderStatusAPIView.as_view(), name="update-order-status"),
    path("user/<int:user_id>/orders/", views.UserOrdersAPIView.as_view(), name="user-orders"),
    path("user/<int:user_id>/order/<int:order_id>/", views.UserOrderDetailAPIView.as_view(), name="user-order-details"),
]