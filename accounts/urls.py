from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.HelloAuthView.as_view(), name="hello"),
    path("register/", views.UserRegisterAPIView.as_view(), name="register"),
]