from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    AmenityForm,
    ContactForm,
    DocumentForm,
    InvoiceForm,
    LeaseForm,
    MaintenanceRecordForm,
    PaymentHistoryForm,
    PropertyForm,
    TenantForm,
)
from .models import (
    Invoice,
    Lease,
    PaymentHistory,
    Property,
    Tenant,
)


def property_list(request):
    properties = Property.objects.all()
    return render(request, "property_list.html", {"properties": properties})

def property_detail(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    return render(request, "property_detail.html", {"property": property_obj})

def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("property_list")
    else:
        form = PropertyForm()
    return render(request, "add_property.html", {"form": form})

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, "tenant_list.html", {"tenants": tenants})

def add_tenant(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tenant_list")
    else:
        form = TenantForm()
    return render(request, "add_tenant.html", {"form": form})

def lease_list(request):
    leases = Lease.objects.all()
    return render(request, "lease_list.html", {"leases": leases})

def add_lease(request):
    if request.method == "POST":
        form = LeaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lease_list")
    else:
        form = LeaseForm()
    return render(request, "add_lease.html", {"form": form})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, "invoice_list.html", {"invoices": invoices})

def add_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invoice_list")
    else:
        form = InvoiceForm()
    return render(request, "add_invoice.html", {"form": form})

def payment_history_list(request):
    payment_histories = PaymentHistory.objects.all()
    return render(request, "payment_history_list.html", {"payment_histories": payment_histories})

def add_payment_history(request):
    if request.method == "POST":
        form = PaymentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("payment_history_list")
    else:
        form = PaymentHistoryForm()
    return render(request, "add_payment_history.html", {"form": form})

def amenity_list(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    amenities = property_obj.amenities.all()
    return render(request, "amenity_list.html", {"amenities": amenities, "property": property_obj})

def add_amenity(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
        form = AmenityForm(request.POST)
        if form.is_valid():
            amenity = form.save(commit=False)
            amenity.property = property_obj
            amenity.save()
            return redirect("amenity_list", property_id=property_id)
    else:
        form = AmenityForm()
    return render(request, "add_amenity.html", {"form": form, "property": property_obj})

def contact_list(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    contacts = tenant.contacts.all()
    return render(request, "contact_list.html", {"tenant": tenant, "contacts": contacts})

def add_contact(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.tenant = tenant
            contact.save()
            return redirect("contact_list", tenant_id=tenant_id)
    else:
        form = ContactForm()
    return render(request, "add_contact.html", {"form": form, "tenant": tenant})

def document_list(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    documents = property_obj.documents.all()
    return render(request, "document_list.html", {"property": property_obj, "documents": documents})

def add_document(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.property = property_obj
            document.save()
            return redirect("document_list", property_id=property_id)
    else:
        form = DocumentForm()
    return render(request, "add_document.html", {"form": form, "property": property_obj})

def maintenance_record_list(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    maintenance_records = property_obj.maintenance_records.all()
    return render(request, "maintenance_record_list.html", {"property": property_obj, "maintenance_records": maintenance_records})

def add_maintenance_record(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
        form = MaintenanceRecordForm(request.POST)
        if form.is_valid():
            maintenance_record = form.save(commit=False)
            maintenance_record.property = property_obj
            maintenance_record.save()
            return redirect("maintenance_record_list", property_id=property_id)
    else:
        form = MaintenanceRecordForm()
    return render(request, "add_maintenance_record.html", {"form": form, "property": property_obj})