from django.db import models

class Property(models.Model):
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
  phone = models.CharField(max_length=15, verbose_name="رقم الهاتف")
  email = models.EmailField(verbose_name="البريد الإلكتروني")

  class Meta:
    verbose_name = "مستأجر"
    verbose_name_plural = "المستأجرون"

  def __str__(self):
    return self.name

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
