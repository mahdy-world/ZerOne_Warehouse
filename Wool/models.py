from django.db import models
from datetime import date
from Auth.models import User
from Core.models import Color

# Create your models here.

class WoolSupplier(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الاضافة")
    name = models.CharField(max_length=50, verbose_name="اسم الشركة")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='رقم الهاتف')
    address = models.CharField(max_length=250, verbose_name='العنوان', null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

WOOL_TYPE = (
    (1,"قطن"),
    (2,"صوف"),
    (3,"عجينة"),
    (4,"سبن"),
    (5,"لكرة"),
    (6,"رمش"),
    (7,"عصب"),
    (8,"بلستر"),
    (9,"استك"),
)


class Wool(models.Model):
    wool_date = models.DateField(null=True, default=date.today, verbose_name="التاريخ")
    wool_name = models.CharField(max_length=50, verbose_name="اسم الخامه")
    wool_type = models.IntegerField(choices=WOOL_TYPE, verbose_name="نوع الخامة")
    wool_number = models.IntegerField(verbose_name="رقم نوع الخامة...")
    wool_weight = models.IntegerField(verbose_name="وزن الخامة...", null=True, blank=True)
    wool_user_created = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="المسئول")
    
    def __str__(self):
        return self.wool_name
    
class WoolColor(models.Model):
    wool = models.ForeignKey(Wool, on_delete=models.CASCADE, verbose_name="الخامة")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="اللون")
    count = models.FloatField(default=0.0, verbose_name="العدد")
    weight = models.FloatField(default=0.0, verbose_name="الوزن")
    
    def __str__(self):
        return f'{self.wool.wool_name} - {self.color.color_name}'

class WoolSupplierQuantity(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ العملية")
    date = models.DateField(null=True, verbose_name="التاريخ", default=date.today)
    supplier = models.ForeignKey(WoolSupplier, on_delete=models.CASCADE, verbose_name="التاجر")
    wool =  models.ForeignKey(Wool, on_delete=models.CASCADE, verbose_name='الخامة')
    wool_color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="اللون")
    wool_item_count = models.FloatField(default=0.0, verbose_name="عدد الشكاير")
    wool_weight = models.FloatField(default=0.0, verbose_name="الوزن بالكيلو")
    wool_loat_number = models.IntegerField(null=True, blank=True, verbose_name="رقم اللوط")
    wool_price = models.FloatField(default=0.0, null=True, blank=True, verbose_name="السعر")
    total_weight = models.FloatField(default=0.0, verbose_name="اجمالي الوزن")
    total_account = models.FloatField(default=0.0, verbose_name="اجمالي الحساب")
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="المسؤول")

    def __str__(self):
        return self.supplier.name
    
    

class WoolSupplierPayment(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ العملية")
    date = models.DateField(null=True, verbose_name="التاريخ", default=date.today)
    supplier = models.ForeignKey(WoolSupplier, on_delete=models.CASCADE, verbose_name="التاجر")
    value = models.FloatField(default=0.0, verbose_name="المبلغ")
    reason = models.CharField(max_length=250, null=True, blank=True, verbose_name='الوصف/السبب')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="المسؤول")

    def __str__(self):
        return self.supplier.name
    


OPERATION_TYPE = (
    (1,"دخول عن طريق مورد"),
    (2,"خروج كمية لفاتورة مبيعات"),
    (3,"دخول مرتجع للمخزن"),
    (4,"حذف كمية بشكل يدوي")
)

    
class WoolOperatoin(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ العملية")
    operation_number = models.IntegerField(null=True, blank=True, verbose_name="رقم العملية")
    operation_type = models.IntegerField(choices=OPERATION_TYPE, verbose_name='نوع العملية')
    operation_wool =  models.ForeignKey(Wool, on_delete=models.CASCADE, verbose_name='الخامة')
    operation_count = models.FloatField(default=0.0, verbose_name="الكمية")
    operation_color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="اللون")
    operation_total_weight = models.FloatField(default=0.0, verbose_name="اجمالي الوزن")
    operation_total_price = models.FloatField(default=0.0, verbose_name="اجمالي الحساب")
    created_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="المسؤول")

    def __str__(self):
        return self.created_date
    
    