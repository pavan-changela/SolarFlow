from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects_home'),
     path('', views.project_list, name='project_list'),
    path('new/', views.create_project, name='create_project'),
]
