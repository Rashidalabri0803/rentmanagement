# Generated by Django 5.1.2 on 2024-11-06 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_owner_maintenancerecord_note_property_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/', verbose_name='ملف المستند')),
                ('description', models.TextField(max_length=255, verbose_name='وصف المستند')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ التحميل')),
                ('lease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='rentals.lease', verbose_name='عقد الإيجار')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='rentals.property', verbose_name='العقار')),
            ],
            options={
                'verbose_name': 'مستند',
                'verbose_name_plural': 'المستندات',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='تاريخ الإصدار')),
                ('due_date', models.DateField(verbose_name='تاريخ الإستحقاق')),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='المبلغ المستحق')),
                ('is_paid', models.BooleanField(default=False, verbose_name='تم السداد')),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='rentals.lease', verbose_name='عقد الإيجار')),
            ],
            options={
                'verbose_name': 'فاتورة',
                'verbose_name_plural': 'الفواتير',
            },
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاريخ الدفع')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='المبلغ المدفوع')),
                ('payment_method', models.CharField(choices=[('cash', 'نقدا'), ('bank', 'تحويل بنكي')], max_length=50, verbose_name='طريقة الدفع')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentals.invoice', verbose_name='الدفعة المرتبطة')),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_histories', to='rentals.lease', verbose_name='عقد الايجار')),
            ],
            options={
                'verbose_name': 'سجل الدفع',
                'verbose_name_plural': 'سجلات الدفع',
            },
        ),
    ]
