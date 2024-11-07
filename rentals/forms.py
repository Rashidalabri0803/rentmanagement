from django import forms

from .models import (
    Amenity,
    Document,
    Invoice,
    Lease,
    MaintenanceRecord,
    Note,
    Payment,
    PaymentHistory,
    Property,
    Tenant,
    Contact,
)

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "dir":"rtl"})
        
class InvoicesForm(forms.ModelForm):
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

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        labels = {
            'property': 'العقار',
            'lease': 'عقد الإيجار',
            'file': 'ملف المستند',
            'description': 'وصف المستند',
        }

class PaymentHistoriesForm(forms.ModelForm):
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

class PropertyForm(BootstrapFormMixin, forms.ModelForm):
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

class ContactForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            "tenant": "المستأجر",
            "name": "اسم جهة الاتصال",
            "relationship": "العلاقة",
            "phone_number": "رقم الهاتف",
        }