from django.urls import path

from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:property_id>/notes/', views.note_list, name='note_list'),
    path('properties/<int:property_id>/notes/add/', views.add_note, name='add_note'),
    path('properties/<int:property_id>/notes/add/', views.add_note, name='add_note'),
    path('properties/<int:property_id>/maintenance/', views.maintenance_list, name='maintenance_list'),
    path('properties/<int:property_id>/maintenance/add/', views.add_maintenance_record, name='add_maintenance_record'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('properties/<int:property_id>/documents/', views.document_list, name='document_list'),
    path('properties/<int:property_id>/documents/add/', views.add_document, name='add_document'),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('leases/', views.lease_list, name='lease_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('add_property/add/', views.add_property, name='add_property'),
]