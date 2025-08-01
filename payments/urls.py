from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='payments_home'),
     path('', views.payment_list, name='payment_list'),
    path('new/', views.create_payment, name='create_payment'),
]
