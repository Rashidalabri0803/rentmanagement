from django.db import models

class Property(models.Model):
  name = models.CharField(max_length=255, verbose_name="اسم العقار")
  address = models.CharField(max_length=255, verbose_name="عنوان العقار")
  description = models.TextField(verbose_name="وصف العقار", blank=True, null=True)
  rent_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الإيجاري")
  is_available = models.BooleanField(default=True, verbose_name="متاح للإيجار")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "عقار"
    verbose_name_plural = "العقارات"

class Tenant(models.Model):
  name = models.CharField(max_length=255, verbose_name="اسم المستأجر")
  email = models.EmailField(verbose_name="البريد الإلكتروني")
  phone_number = models.CharField(max_length=20, verbose_name="رقم الهاتف")
  property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="العقار المستأجر")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "مستأجر"
    verbose_name_plural = "المستأجرون"

class Payment(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name="المستأجر")
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ المدفوع")
  payment_date = models.DateField(verbose_name="تاريخ الدفع")
  notes = models.TextField(verbose_name="ملاحظات", blank=True, null=True)

  def __str__(self):
    return f"{self.amoune} - {self.tenant.name}"

  class Meta:
    verbose_name = "دفعة"
    verbose_name_plural = "الدفعات"