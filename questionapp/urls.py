from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
   
]