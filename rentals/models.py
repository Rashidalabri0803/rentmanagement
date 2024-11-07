from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Owner(models.Model):
  name = models.CharField(max_length=200, verbose_name="اسم المالك")
  phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")
  email = models.EmailField(verbose_name="البريد الإلكتروني")
  address = models.TextField(verbose_name="عنوان المالك", blank=True)

  class Meta:
    verbose_name = "مالك"
    verbose_name_plural = "المالكون"

  def __str__(self):
    return self.name
    
class Property(models.Model):
  owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, verbose_name="المالك")
  name = models.CharField(max_length=200, verbose_name="اسم العقار")
  address = models.TextField(verbose_name="عنوان العقار")
  price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الإيجار الشهري")
  tags = models.ManyToManyField("Tag", blank=True, related_name="properties", verbose_name="التصنيفات")

  class Meta:
    verbose_name = "عقار"
    verbose_name_plural = "العقارات"

  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True, verbose_name="وصف التصنيف")

  class Meta:
    verbose_name = "تصنيف"
    verbose_name_plural = "التصنيفات"

  def __str__(self):
    return self.name
    
class Tenant(models.Model):
  name = models.CharField(max_length=100, verbose_name="اسم المستأجر")
  phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")
  email = models.EmailField(verbose_name="البريد الإلكتروني")
  rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True, verbose_name="تقييم المستأجر")



  class Meta:
    verbose_name = "مستأجر"
    verbose_name_plural = "المستأجرون"

  def __str__(self):
    return self.name

class TenantReview(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="reviews", verbose_name="المستأجر")
  review_name = models.CharField(max_length=100, verbose_name="اسم المراجع")
  review_date = models.DateField(verbose_name="تاريخ المراجعة")
  rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="التقييم")
  comment = models.TextField(verbose_name="التعليق")

  class Meta:
    verbose_name = "مراجعة المستأجر"
    verbose_name_plural = "المراجعات المستأجرين"

  def __str__(self):
    return f"مراجعة لــ {self.tenant.name} - {self.rating} نجوم"
    
class Lease(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="العقار")
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name="المستأجر")
  start_date = models.DateField(verbose_name="تاريخ البدء الإيجار")
  end_date = models.DateField(verbose_name="تاريخ النهاية الإيجار")
  monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإيجار الشهري")
  security_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="التأمين")

  class Meta:
    verbose_name = "عقد إيجار"
    verbose_name_plural = "عقود الإيجار"

  def __str__(self):
    return f"{self.property} - {self.tenant}"

class Invoice(models.Model):
  lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name="invoices", verbose_name="عقد الإيجار")
  date_issued = models.DateField(verbose_name="تاريخ الإصدار")
  due_date = models.DateField(verbose_name="تاريخ الإستحقاق")
  amount_due = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ المستحق")
  is_paid = models.BooleanField(default=False, verbose_name="تم السداد")
  late_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="رسوم التأخير")

  class Meta:
    verbose_name = "فاتورة"
    verbose_name_plural = "الفواتير"

  def __str__(self):
    return f"فاتورة - {self.lease} - {self.amount_due}"

  def apply_late_fee(self):
    """تطبيق رسوم تأخير إذا كانت الفاتورة غير مدفوعة وتجاوزت تاريخ الاستحقاق"""
    if not self.is_paid and self.due_date < timezone.now().date():
      self.amount_due += self.late_fee
      self.save()

class PaymentHistory(models.Model):
  lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name="payment_histories", verbose_name="عقد الايجار")
  date = models.DateField(verbose_name="تاريخ الدفع")
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ المدفوع")
  payment_method = models.CharField(max_length=50, choices=[("cash", "نقدا"), ("bank", "تحويل بنكي")], verbose_name="طريقة الدفع")
  invoice = models.ForeignKey("Invoice", on_delete=models.SET_NULL, null=True, blank=True, verbose_name= "الدفعة المرتبطة")

  class Meta:
    verbose_name = "سجل الدفع"
    verbose_name_plural = "سجلات الدفع"

  def __str__(self):
    return f"دفعة {self.amount} - {self.date}"

class Amenity(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name = "amenities", verbose_name="العقار")
  name = models.CharField(max_length=100, verbose_name="اسم المرفق")
  description = models.TextField(verbose_name="وصف المرفق", blank=True)

  class Meta:
    verbose_name = "مرفق"
    verbose_name_plural = "المرفقات"

  def __str__(self):
    return f"{self.name} - {self.property.name}"

class Contact(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="contacts", verbose_name="المستأجر")
  name = models.CharField(max_length=100, verbose_name="اسم جهة الاتصال")
  relationship = models.CharField(max_length=50, verbose_name="العلاقة")
  phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")

  class Meta:
    verbose_name = "جهة اتصال"
    verbose_name_plural = "جهات الاتصال"

  def __str__(self):
    return f"جهة اتصال: {self.tenant.name} - المستأجر: {self.tenant.name}"
    
class Document(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="documents", verbose_name="العقار")
  lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name="documents", null=True, blank=True, verbose_name="عقد الإيجار")
  file = models.FileField(upload_to="documents/", verbose_name="ملف المستند")
  description = models.TextField(max_length=255, verbose_name="وصف المستند")
  uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التحميل")

  class Meta:
    verbose_name = "مستند"
    verbose_name_plural = "المستندات"

  def __str__(self):
    return f"مستند للعقار: {self.property.name} - {self.description}"

class MaintenanceRecord(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="maintenance_records", verbose_name="العقار")
  description = models.TextField(verbose_name="وصف الصيانة")
  date = models.DateField(verbose_name="تاريخ الصيانة")
  cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="تكلفة الصيانة")
  is_completed = models.BooleanField(default=False, verbose_name="تم الإنجاز")

  class Meta:
    verbose_name = "سجل الصيانة"
    verbose_name_plural = "سجلات الصيانة"

  def __str__(self):
    return f"صيانة: {self.description} - {self.property.name}"

class Note(models.Model):
  property = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="notes", verbose_name="العقار")
  tenant = models.ForeignKey("Tenant", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المستأجر")
  content = models.TextField(verbose_name="محتوى الملاحظة")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

  class Meta:
    verbose_name = "ملاحظة"
    verbose_name_plural = "الملاحظات"

  def __str__(self):
    return f"ملاحظات للعقار: {self.property.name}"

class Payment(models.Model):
  lease = models.ForeignKey("Lease", on_delete=models.CASCADE, verbose_name="العقد")
  date = models.DateField(verbose_name="تاريخ الدفع")
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قيمة الدفع")
  method = models.CharField(max_length=50, verbose_name="طريقة الدفع", choices=[("cash", "نقدا"), ("bank", "تحويل بنكي")])
  
  class Meta:
    verbose_name = "دفعة"
    verbose_name_plural = "دفعات"

  def __str__(self):
    return f"{self.lease} - {self.amount}"