from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.

class Object(models.Model):
    name = models.CharField(_('object name'), max_length=200)
    company = models.CharField(_('object company name'), max_length=200)
    category = models.CharField(_('object category'), max_length=200)
    specifications = models.CharField(_('object specifications') , max_length=1000)
    image = models.ImageField(_('object image') , upload_to='db/images/%Y/%m/%d/' ,height_field=None, width_field=None, max_length=200)
    sheet = models.FileField(_('object sheet') , upload_to='db/sheet/%Y/%m/%d/', max_length=200 , blank=True , null=True)
    created_at = models.DateTimeField( blank=True , null=True)
    updated_at = models.DateTimeField( blank=True , null=True)

# class ContactUs(models.Model):
#     title = models.CharField(_('title of message') , max_length=200)
#     description = models.TextField(_('description of message'))
#     published_at = models.DateTimeField(auto_now_add=True)