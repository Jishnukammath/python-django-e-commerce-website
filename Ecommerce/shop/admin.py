from django.contrib import admin
from . models import *
# Register your models here.
class catagadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,catagadmin)


class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','img','stock','price']
    list_editable=['img','stock','price']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodadmin)