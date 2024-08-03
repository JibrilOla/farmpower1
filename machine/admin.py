from django.contrib import admin
from .models import MachinePurchase
# Register your models here.
class MachinePurchaseAdmin(admin.ModelAdmin):
    list_display = ["user","price","purchase_date","end_date","remaining_days","income"]
admin.site.register(MachinePurchase)