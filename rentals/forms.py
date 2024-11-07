from django import forms

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


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "dir":"rtl"})

class OwnerForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
        labels = {
            'name': 'اسم المالك',
            'phone_number': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
            'address': 'عنوان المالك',
        }

class PropertyForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        labels = {
            'owner': 'المالك',
            'name': 'اسم العقار',
            'address': 'عنوان العقار',
            'price': 'سعر الإيجار الشهري',
        }

class TenantForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'
        labels = {
            'name': 'اسم المستأجر',
            'phone_number': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
        }

class LeaseForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Lease
        fields = '__all__'
        labels = {
            'property': 'العقار',
            'tenant': 'المستأجر',
            'start_date': 'تاريخ البدء الإيجار',
            'end_date': 'تاريخ النهاية الإيجار',
            'monthly_rent': 'الإيجار الشهري',
        }

class InvoiceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        labels = {
            'lease': 'عقد الإيجار',
            'date_issued': 'تاريخ الإصدار',
            'due_date': 'تاريخ الإستحقاق',
            'amount_due': 'المبلغ المستحق',
            'is_paid': 'تم السداد',
        }

class PaymentHistoryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PaymentHistory
        fields = '__all__'
        labels = {
            'lease': 'عقد الإيجار',
            'date': 'تاريخ الدفع',
            'amount': 'المبلغ المدفوع',
            'payment_method': 'طريقة الدفع',
            'invoice': 'الدفعة المرتبطة',
        }

class AmenityForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Amenity
        fields = '__all__'
        labels = {
            'property': 'العقار',
            'name': 'اسم المرفق',
            'description': 'وصف المرفق',
        }

class ContactForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'tenant': 'المستأجر',
            'name': 'اسم جهة الاتصال',
            'relationship': 'العلاقة',
            'phone_number': 'رقم الهاتف',
        }

class DocumentForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        labels = {
            'property': 'العقار',
            'lease': 'عقد الإيجار',
            'file': 'ملف المستند',
            'description': 'وصف المستند',
        }

class MaintenanceRecordForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
        labels = {
            'property': 'العقار',
            'description': 'وصف الصيانة',
            'date': 'تاريخ الصيانة',
            'cost': 'تكلفة الصيانة',
            'is_completed': 'تم الإنجاز',
        }