from django.db import models

class Owner(models.Model):
  name = models.CharField(max_length=200, verbose_name="اسم المالك")
  phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")
  email = models.EmailField(verbose_name="البريد الإلكتروني")
  address = models.CharField(max_length=200, verbose_name="عنوان المالك")

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

  class Meta:
    verbose_name = "عقار"
    verbose_name_plural = "العقارات"

  def __str__(self):
    return self.name

class Tenant(models.Model):
  name = models.CharField(max_length=100, verbose_name="اسم المستأجر")
  phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")
  email = models.EmailField(verbose_name="البريد الإلكتروني")

  class Meta:
    verbose_name = "مستأجر"
    verbose_name_plural = "المستأجرون"

  def __str__(self):
    return self.name

class Note(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="notes", verbose_name="العقار")
  tenant = models.ForeignKey("Tenant", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المستأجر")
  content = models.TextField(verbose_name="محتوى الملاحظة")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

  class Meta:
    verbose_name = "ملاحظة"
    verbose_name_plural = "الملاحظات"

  def __str__(self):
    return f"ملاحظات للعقار: {self.property.name}"

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


class Amenity(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name = "amenities", verbose_name="العقار")
  name = models.CharField(max_length=100, verbose_name="اسم المرفق")
  description = models.TextField(verbose_name="وصف المرفق", blank=True)

  class Meta:
    verbose_name = "مرفق"
    verbose_name_plural = "المرفقات"

  def __str__(self):
    return f"{self.name} - {self.property.name}"

class Lease(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="العقار")
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name="المستأجر")
  start_date = models.DateField(verbose_name="تاريخ البدء الإيجار")
  end_date = models.DateField(verbose_name="تاريخ النهاية الإيجار")
  monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإيجار الشهري")

  class Meta:
    verbose_name = "عقد إيجار"
    verbose_name_plural = "عقود الإيجار"

  def __str__(self):
    return f"{self.property} - {self.tenant}"

class Payment(models.Model):
  lease = models.ForeignKey(Lease, on_delete=models.CASCADE, verbose_name="العقد")
  date = models.DateField(verbose_name="تاريخ الدفع")
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قيمة الدفع")
  method = models.CharField(max_length=50, verbose_name="طريقة الدفع", choices=[("cash", "نقدا"), ("bank", "تحويل بنكي")])
  
  class Meta:
    verbose_name = "دفعة"
    verbose_name_plural = "دفعات"

  def __str__(self):
    return f"{self.lease} - {self.amount}"