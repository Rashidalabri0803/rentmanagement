from django import forms

from .models import (
    Amenity,
    Lease,
    MaintenanceRecord,
    Note,
    Payment,
    Property,
    Tenant,
)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
        labels = {
            "property": "العقار",
            "tenant": "المستأجر",
            "content": "محتوى الملاحظة",
        }

class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = "__all__"
        labels = {
            "property": "العقار",
            "description": "وصف الصيانة",
            "date": "تاريخ الصيانة",
            "cost": "تكلفة الصيانة",
            "is_completed": "تم الإنجاز",
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
        labels = {
            "name": "اسم العقار",
            "address": "عنوان العقار",
            "price": "سعر الإيجار الشهري",
        }

class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = "__all__"
        labels = {
            "property": "العقار",
            "name": "اسم المرفق",
            "description": "وصف المرفق",
        }

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = "__all__"
        labels = {
            "name": "اسم المستأجر",
            "phone_number": "رقم الهاتف",
            "email": "البريد الإلكتروني",
        }

class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = "__all__"
        labels = {
            "property": "العقار",
            "tenant": "المستأجر",
            "start_date": "تاريخ البدء الإيجار",
            "end_date": "تاريخ النهاية الإيجار",
            "monthly_rent": "الإيجار الشهري",
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        labels = {
            "lease": "عقد الايجار",
            "date": "تاريخ الدفع",
            "amount": "قيمة الدفع",
            "method": "طريقة الدفع",
        }