from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('quotation/', include('quotation.urls')),
    path('', views.dashboard, name='dashboard'),
    path('projects/', include('projects.urls')),
    path('service/', include('service.urls')),
    path('orderbook/', include('orderbook.urls')),
    path('payments/', include('payments.urls')),
]
