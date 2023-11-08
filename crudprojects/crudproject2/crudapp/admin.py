from django.contrib import admin
from crudapp.models import Product
class productAdmin(admin.ModelAdmin):
	list_display=['pno','name','price','warenty']
admin.site.register(Product,productAdmin)
# Register your models here.
