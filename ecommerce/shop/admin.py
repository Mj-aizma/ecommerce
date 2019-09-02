from django.contrib import admin

from .models import Object
# Register your models here.

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name' , 'company' , 'category')
    list_filter = ('category' , 'company')
    search_fields = ('name' , 'company' , 'category')