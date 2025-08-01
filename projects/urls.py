from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),  # Use this as home
    path('new/', views.create_project, name='create_project'),
]
