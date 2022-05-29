from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from commons.models import TimestampModel,UserstampModel

# Create your models here.


class Profile(TimestampModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("user"))
    image = models.ImageField(upload_to='profile',verbose_name=_("image"),default='profile.jpg')
    token = models.CharField(max_length=255,default=None,blank=True,null=True,verbose_name=_('token'))


    def __str__(self) -> str:
        return str(self.user.username)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ["-id"]


class Otp(TimestampModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("user"))
    otp = models.PositiveBigIntegerField()
    is_verified= models.BooleanField(default=False)








