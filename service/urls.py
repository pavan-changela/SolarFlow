from django.urls import path
from . import views

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('new/', views.create_complaint, name='create_complaint'),
]
