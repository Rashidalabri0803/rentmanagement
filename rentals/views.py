from django.shortcuts import redirect, render

from .forms import PropertyForm, TenantForm, LeaseForm
from .models import Lease, Property, Tenant, Amenity, Payment


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

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