from django.db import models

class Tenant(models.Model):
    name = models.CharField(verbose_name="اسم المستأجر", max_length=100)
    phone = models.CharField(verbose_name="رقم الهاتف", max_length=15)
    email = models.EmailField(verbose_name="البريد الإلكتروني", blank=True, null=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    address = models.CharField(verbose_name="عنوان العقار", max_length=255)
    rent_price = models.DecimalField(verbose_name="سعر الإيجار", max_digits=10, decimal_places=2)
    tenant = models.ForeignKey(Tenant, verbose_name="المستأجر", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.address

class Payment(models.Model):
    property = models.ForeignKey(Property, verbose_name="العقار", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="تاريخ الدفع")
    amount = models.DecimalField(verbose_name="المبلغ", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.amount} - {self.property.address}"