from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Object(models.Model):
    name = models.CharField(_('object name'), max_length=200)
    company = models.CharField(_('object company name'), max_length=200)
    category = models.CharField(_('object category'), max_length=200)
    Specifications = models.CharField(_('object Specifications') , max_length= 1000)

