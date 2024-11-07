from django.contrib import admin

from .models import (
    Amenity,
    Contact,
    Document,
    Invoice,
    Lease,
    MaintenanceRecord,
    Owner,
    PaymentHistory,
    Property,
    Tenant,
)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'phone_number', 'email')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'price')
    search_fields = ('name', 'address')
    list_filter = ('owner',)

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'phone_number', 'email')

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'start_date', 'end_date', 'monthly_rent')
    list_filter = ('start_date', 'end_date', 'property', 'tenant')
    search_fields = ('property__name', 'tenant__name')
    date_hierarchy = 'start_date'

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('lease', 'date_issued', 'due_date', 'amount_due', 'is_paid')
    list_filter = ('is_paid', 'due_date')
    search_fields = ('lease__property__name', 'lease__tenant__name')
    list_editable = ('is_paid',)
    date_hierarchy = 'due_date'

@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('lease', 'date', 'amount', 'payment_method', 'invoice')
    list_filter = ('payment_method', 'date')
    search_fields = ('lease__property__name', 'lease__tenant__name')
    date_hierarchy = 'date'

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'property', 'description')
    search_fields = ('name', 'property__name')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'name', 'relationship', 'phone_number')
    search_fields = ('tenant__name', 'name', 'phone_number')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('property', 'lease', 'description', 'uploaded_at')
    search_fields = ('property__name', 'description')
    list_filter = ('uploaded_at',)

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('property', 'description', 'date', 'cost', 'is_completed')
    list_filter = ('is_completed', 'date', 'property')
    search_fields = ('property__name', 'description')
    list_editable = ('is_completed',)
    date_hierarchy = 'date'