from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('main', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
