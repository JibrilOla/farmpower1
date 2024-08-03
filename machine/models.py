from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


class MachinePurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True)
    machine_name = models.CharField(max_length=200, null=True)
    is_verified = models.BooleanField(default=False)
    purchase_date = models.DateTimeField(auto_now_add=True, null=True)
    end_date = models.DateTimeField(default=timezone.now() + timedelta(days=30))
    remaining_days = models.IntegerField(default=30)
    income = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    revenue = models.DecimalField(default=0, max_digits=12, decimal_places=2)

