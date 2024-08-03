from django.contrib import admin
from .models import Profile
from machine.models import MachinePurchase


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created")


