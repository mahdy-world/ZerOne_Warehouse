from django.utils.timezone import now
from django.contrib.auth.models import User
from Products.models import *
from Wool.models import Wool
from Core.models import Color

# Create your models here.

invoice_choices = (
    (1, "فاتورة مبيعات"),
    (2, "فاتورة مرتجع مبيعات"),
    (3, "مبيعات مستقلة"),
)

class Invoice(models.Model):
    date = models.DateField(default=now, verbose_name='التاريخ')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='منشئ الفاتورة')
    invoice_type = models.IntegerField(choices=invoice_choices, default=0, verbose_name='نوع الفاتورة')
    seller = models.ForeignKey(ProductSellers, on_delete=models.CASCADE, null=True, verbose_name='العميل')
    customer = models.CharField(max_length=255, verbose_name='العميل')
    total = models.FloatField(default=0.0, verbose_name='قيمة الفاتورة')
    discount = models.FloatField(default=0.0, verbose_name='الخصم')
    old_value = models.FloatField(default=0.0, verbose_name='حساب قديم')
    # return_value = models.FloatField(default=0.0, verbose_name='مرتجع بقيمة')
    paid_value = models.FloatField(default=0.0, verbose_name='دفعة بقيمة')
    overall = models.FloatField(default=0.0, verbose_name='الإجمالي')
    comment = models.TextField(null=True, blank=True, verbose_name="ملاحظات")
    saved = models.BooleanField(default=False, verbose_name='حفظ')
    close = models.BooleanField(default=False, verbose_name='اغلاق')
    deleted = models.BooleanField(default=False, verbose_name='حذف')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاريخ العملية")
    check_date = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الشيك ")
    check_value = models.FloatField(default=0.0, null=True, blank=True,  verbose_name='قيمة الشيك')

    def __str__(self):
        return str(self.id)


UNIT_CHOICES = (
    (1, 'قطعة'),
)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='الفاتورة')
    item = models.ForeignKey(Wool, on_delete=models.SET_NULL, null=True, verbose_name='الصنف')
    unit_price = models.FloatField(default=0.0, verbose_name='سعر البيع')
    quantity = models.FloatField(default=1.0, verbose_name='الكمية')
    wool_weight = models.FloatField(default=0.0, verbose_name='وزن الوحدة')
    total_weight = models.FloatField(default=0.0, verbose_name='اجمالي الوزن')
    total_price = models.FloatField(default=0.0, verbose_name='اجمالي الحساب')
    deleted = models.BooleanField(default=False, verbose_name='حذف المنتج من الفاتورة')
    wool_color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='اللون')
    date = models.DateField(default=now, verbose_name='التاريخ')

    def __str__(self):
        return str(self.invoice.id)


# class InvoiceItemDetails(models.Model):
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='الفاتورة')
#     invoice_item = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE, verbose_name='عنصر الفاتورة')
#     item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='الصنف')
#     unit_price = models.FloatField(default=0.0, verbose_name='سعر البيع')
#     quantity = models.FloatField(default=0, verbose_name='الكمية المرتجعة')
#     unit = models.IntegerField(choices=UNIT_CHOICES, default=0, verbose_name='الوحدة')
#     total_price = models.FloatField(default=0.0, verbose_name='إجمالي')
#     deleted = models.BooleanField(default=False, verbose_name='حذف المنتج من المرتجع')
#     date = models.DateField(default=now, verbose_name='التاريخ')
#
#     def __str__(self):
#         return str(self.invoice.id)