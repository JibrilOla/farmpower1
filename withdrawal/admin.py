from django.contrib import admin
from .models import Withdrawal


@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ("user", "withdrawal_amount", "status", "date_placed")
    list_filter = ("status",)
    actions = ["verify_withdrawals"]

    def save_model(self, request, obj, form, change):
        # Perform additional logic when saving the withdrawal record
        if obj.status == "success":
            # Additional logic when the withdrawal is verified
            # For example, update the user's balance or send notifications
            pass

        super().save_model(request, obj, form, change)

    def verify_withdrawals(self, request, queryset):
        queryset.update(status="success")
        self.message_user(
            request, "Selected withdrawals have been verified successfully."
        )

    verify_withdrawals.short_description = "Verify selected withdrawals"
