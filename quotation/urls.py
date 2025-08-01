from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotation_redirect, name='quotation_home'),  # NEW default redirect
    path('new/', views.create_quotation, name='create_quotation'),
    path('success/', views.quotation_success, name='quotation_success'),
    path('<int:quotation_id>/pdf/', views.quotation_pdf, name='quotation_pdf'),
]
