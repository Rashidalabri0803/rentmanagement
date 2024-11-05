from django.shortcuts import get_object_or_404, redirect, render

from .forms import PropertyForm, TenantForm, LeaseForm, NoteForm, MaintenanceRecordForm, AmenityForm, PaymentForm
from .models import Lease, Property, Tenant, Amenity, Payment, MaintenanceRecord, Note


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def note_list(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    notes = property_obj.notes.all()
    return render(request, 'note_list.html', {'property': property_obj, 'notes': notes})

def add_note(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.property = property_obj
            note.save()
            return redirect('note_list', property_id=property_id)
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form, 'property': property_obj})

def maintenance_list(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    maintenance_records = property_obj.maintenance_records.all()
    return render(request, 'maintenance_list.html', {'property': property_obj, 'maintenance_records': maintenance_records})

def add_maintenance_record(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = MaintenanceRecordForm(request.POST)
        if form.is_valid():
            maintenance_record = form.save(commit=False)
            maintenance_record.property = property_obj
            maintenance_record.save()
            return redirect('maintenance_list', property_id=property_id)
    else:
        form = MaintenanceRecordForm()
    return render(request, 'add_maintenance_record.html', {'form': form, 'property': property_obj})

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

def lease_list(request):
    leases = Lease.objects.all()
    return render(request, 'lease_list.html', {'leases': leases})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})