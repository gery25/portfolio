from django.contrib import admin
from django.urls import path 
from developer_portfolio import views

urlpatterns = [
    path('', views.home, name='home'),
]
