from django.db import models

# Create your models here.

Balance_Type = (
    (1, "للعميل"),
    (2, "علي العميل"),
    )

class Customer(models.Model):
    customer_name = models.CharField(max_length=250, verbose_name='اسم العميل')
    customer_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='رقم الهاتف')
    customer_address = models.CharField(max_length=250, verbose_name='العنوان', null=True, blank=True)
    customer_id_number = models.CharField(max_length=14, verbose_name='الرقم القومي', null=True, blank=True)
    initial_balance_debit = models.FloatField(default=0, verbose_name='القيمة الافتتاحية')
    initial_balance_type = models.IntegerField(choices=Balance_Type, default=0, verbose_name="نوع القيمة الافتتاحية")
    deleted = models.BooleanField(default=False, verbose_name='حذف')
    agreement = models.TextField(verbose_name='اتفاق مسبق', null=True, blank=True)

    def __str__(self):
        return self.name    