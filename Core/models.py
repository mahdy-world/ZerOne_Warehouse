from django.db import models


# Create your models here.

class SystemInformation(models.Model):
    logo = models.ImageField(null=True, blank=True, verbose_name="شعارالنظام")
    name = models.CharField(null=True, max_length=50, verbose_name="اسم النظام")
    type = models.CharField(null=True, max_length=50, verbose_name="نوع النظام")
    manage = models.CharField(null=True, max_length=50, verbose_name="إدارة")
    phone = models.CharField(null=True, max_length=11, verbose_name="هاتف 1")
    phone2 = models.CharField(null=True, blank=True, max_length=11, verbose_name="هاتف 2")
    address = models.CharField(max_length=150, null=True, verbose_name="العنوان")
    geo_site = models.CharField(max_length=150, null=True, blank=True, verbose_name="موقعك الجغرافي")

    def __str__(self):
        return 'معلومات النظام'
    
    
class Modules(models.Model):
    seller_active = models.BooleanField(default=True, verbose_name="تنشيط التجار")
    invoice_active = models.BooleanField(default=True, verbose_name="تنشيط الفواتير ")
    treasury_active = models.BooleanField(default=True, verbose_name="تنشيط الخزائن")
    wool_active = models.BooleanField(default=True, verbose_name="تنشيط الخيط")
    stop_date = models.DateField(null=True, blank=True, verbose_name="فترة تجريبية")

    def __str__(self):
        return 'عناصر النظام'
    
class Color(models.Model):
    color_name = models.CharField(max_length=50, verbose_name="اسم اللون")
    color_hex_code = models.CharField(max_length=7, verbose_name="كود اللون")
    
    def __str__(self):
        return self.color_name