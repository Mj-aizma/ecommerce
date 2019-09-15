from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(_('title of message') , max_length=200)
    description = models.TextField(_('description of message'))
    published_at = models.DateTimeField(auto_now_add=True)