from django.contrib import admin
from .models import Property, Tenant, Lease

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "price")
    search_fields = ("name", "address")

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email")
    search_fields = ("name", "phone_number", "email")

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ("property", "tenant", "start_date", "end_date", "monthly_rent")
    list_filter = ("start_date", "end_date")
    search_fields = ("property__name", "tenant__name")