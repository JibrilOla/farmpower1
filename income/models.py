from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ButtonClick(models.Model):
    clicked = models.BooleanField(default=False)
    last_clicked = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default=None)
    machine_name = models.CharField(max_length=200, null=True)
    ref_income = models.CharField(max_length=200, default=0)

    class Meta:
        unique_together = ["user", "machine_name"]


class RecommendationsIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.amount}"
