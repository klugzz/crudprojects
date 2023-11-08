from django.contrib import admin
from crudapp.models import Bank
class BankAdmin(admin.ModelAdmin):
	list_display=['acno','name','depamnt','bal']
admin.site.register(Bank,BankAdmin)

# Register your models here.
