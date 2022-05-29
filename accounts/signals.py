from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

 
@receiver(post_save,sender=Topup)
def update_account_head_on_topup(sender,instance,created,**kwargs):
    if created:
        account_head,created = AccountHead.objects.get_or_create(id=1)
        old_remaining_amount = int(account_head.remaining_amount)
        old_topup_amount = int(account_head.total_topup_amount)

        new_remaining_amount = old_remaining_amount + instance.amount
        new_topup_amount = old_topup_amount + instance.amount

        account_head.remaining_amount = new_remaining_amount
        account_head.total_topup_amount = new_topup_amount
        account_head.save()
         

@receiver(post_save,sender=ExpenseItem)
def update_account_head_on_expense(sender,instance,created,**kwargs):
    if created:
        account_head,created = AccountHead.objects.get_or_create(id=1)
        old_expense_amount = account_head.total_expense_amount
        old_remaining_amount = account_head.remaining_amount

        new_remaining_amount = old_remaining_amount - (instance.quantity*instance.price)
        new_expense_amount = old_expense_amount + (instance.quantity*instance.price)

        account_head.remaining_amount = new_remaining_amount
        account_head.total_expense_amount = new_expense_amount
        account_head.save()

        

        






 
