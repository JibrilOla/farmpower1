from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Payment, UserWallet
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from registration.models import Profile
from machine.models import MachinePurchase
from withdrawal.models import Withdrawal


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "ref", "amount", "verified", "date_created"]


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


class MachinePurchaseInline(admin.TabularInline):
    model = MachinePurchase
    fk_name = "user"
    extra = 0
class WithdrawalInline(admin.TabularInline):
    model = Withdrawal
    fk_name = "user"
    extra = 0


class ProfileInline(admin.TabularInline):
    model = Profile
    fk_name = "user"
    extra = 0


class UserWalletInline(admin.TabularInline):
    model = UserWallet
    fk_name = "user"
    extra = 0


class CustomUserAdmin(UserAdmin):
    inlines = [PaymentInline, ProfileInline, UserWalletInline, MachinePurchaseInline,WithdrawalInline]


admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserWallet)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
