from django.db import models
from django.utils.translation import gettext_lazy as _
from commons.models import TimestampModel,UserstampModel

# Create your models here.


class ExpenseTitle(TimestampModel,UserstampModel):
    name = models.CharField(max_length=100, unique=True,verbose_name=_("name"))
    enable = models.BooleanField(default=True,verbose_name=_("enabled"))

    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        verbose_name =_("Expense Title")
        verbose_name_plural = _("Expense Titles")
        ordering = ["-id"]

class Expense(TimestampModel,UserstampModel):
    name = models.CharField(max_length=100,unique=True,verbose_name=_("name"))
    expense_title = models.ForeignKey(ExpenseTitle,on_delete=models.CASCADE,verbose_name=_("expense title"))
    bill_image = models.ImageField(upload_to='bills',blank=True,null=True,default='bill.jpeg',verbose_name=_("bill image"))

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name =_("Expense")
        verbose_name_plural =_("Expenses")
        ordering = ["-id"]


class ExpenseItem(TimestampModel,UserstampModel):
    name = models.CharField(max_length=100,unique=True,verbose_name=_("name"))
    expense = models.ForeignKey(Expense,on_delete=models.CASCADE,verbose_name=_("expense"),related_name='expense_items')
    quantity = models.PositiveIntegerField(verbose_name=_("quantity"))
    price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("unit_price"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Expense Item")
        verbose_name_plural = _("Expense Items")
        ordering = ["-id"]


class Topup(TimestampModel,UserstampModel):
    amount = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("amount"))

    def __str__(self) -> str:
        return str(self.amount)

    class Meta:
        verbose_name = _("Top UP")
        verbose_name_plural = _("Top Ups")
        ordering = ["-id"]

class AccountHead(TimestampModel,UserstampModel):
    total_expense_amount = models.DecimalField(max_digits=5,decimal_places=3,default=0,verbose_name=_("total expense amount"))
    remaining_amount = models.DecimalField(max_digits=5,decimal_places=3,default=0,verbose_name=_("remaining amount"))
    total_expense_amount = models.DecimalField(max_digits=5,decimal_places=3,default=0,verbose_name=_("total topup amount"))

    def __str__(self) -> str:
        return str(self.total_expense_amount)

    class Meta:
        verbose_name = _("Account Head")
        verbose_name_plural = _("Account Heads")
        ordering = ["-id"]











