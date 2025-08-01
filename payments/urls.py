from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),   # keep only one ''
    path('new/', views.create_payment, name='create_payment'),
]
