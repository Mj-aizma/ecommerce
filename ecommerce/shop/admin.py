from django.contrib import admin

from .models import Object , Tag
# from .models import ContactUs
# Register your models here.


class TagInline(admin.TabularInline):
    model = model = Object.tag.through
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name' , 'company' , 'category')
    list_filter = ('category' , 'company')
    search_fields = ('name' , 'company' , 'category')

    inlines = [TagInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # pass


