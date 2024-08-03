from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets
from .paystack import Paystack
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserWallet(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, default="NGN")
    balance = models.PositiveIntegerField(default=200)
    created_at = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.user.__str__()

    @receiver(post_save, sender=User)
    def create_user_wallet(sender, instance, created, **kwargs):
        if created:
            UserWallet.objects.create(user=instance)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default="False")
    date_created = models.DateTimeField(auto_now_add="True")

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref

        super().save(*args, **kwargs)

    def amount_value(self):
        return int(self.amount) * 100

    def verifypayment(self):
        paystack = Paystack()
        status, result = paystack.verifypayment(self.ref, self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False
