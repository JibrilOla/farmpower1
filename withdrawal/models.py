from django.contrib.auth.models import User
from django.db import models

class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    withdrawal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_holder_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='pending')
    date_placed=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"Withdrawal{self.pk}-{self.user.username}"