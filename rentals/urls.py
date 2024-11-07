from django.urls import path

from . import views

urlpatterns = [
    path("properties/", views.property_list, name="property_list"),
    path("properties/add/", views.add_property, name="add_property"),
    path("properties/<int:property_id>/", views.property_detail, name="property_detail"),

    path("tenants/", views.tenant_list, name="tenant_list"),
    path("tenants/add/", views.add_tenant, name="add_tenant"),

    path("leases/", views.lease_list, name="lease_list"),
    path("leases/add/", views.add_lease, name="add_lease"),

    path("invoices/", views.invoice_list, name="invoice_list"),
    path("invoices/add/", views.add_invoice, name="add_invoice"),

    path("payments/", views.payment_history_list, name="payment_history_list"),
    path("payments/add/", views.add_payment_history, name="add_payment"),

    path("properties/<int:property_id>/amenities/", views.amenity_list, name="amenity_list"),
    path("properties/<int:property_id>/amenities/add/", views.add_amenity, name="add_amenity"),

    path("tenants/<int:tenant_id>/contacts/", views.contact_list, name="contact_list"),
    path("tenants/<int:tenant_id>/contacts/add/", views.add_contact, name="add_contact"),

    path("properties/<int:property_id>/documents/", views.document_list, name="document_list"),
    path("properties/<int:property_id>/documents/add/", views.add_document, name="add_document"),

    path("properties/<int:property_id>/maintenance/", views.maintenance_record_list, name="maintenance_record_list"),
    path("properties/<int:property_id>/maintenance/add/", views.add_maintenance_record, name="add_maintenance_record"),
]