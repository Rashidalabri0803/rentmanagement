from django.urls import path

from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('leases/', views.lease_list, name='lease_list'),
    path('add_property/add/', views.add_property, name='add_property'),
]