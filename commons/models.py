from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,verbose_name =_("created at"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name =_("updateded at"))

    class Meta:
        abstract = True


class UserstampModel(models.Model):
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True,default= None,verbose_name=_("created by"),
        related_name="+"
        )
    updated_by = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True,default= None,verbose_name=_("updated by"),
        related_name="+"
        )
    class Meta:
        abstract = True
















