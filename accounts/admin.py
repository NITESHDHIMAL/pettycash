import imp
from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(ExpenseTitle)
admin.site.register(Expense)
admin.site.register(ExpenseItem)
admin.site.register(Topup)
admin.site.register(AccountHead)


