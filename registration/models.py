from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code
from machine.models import MachinePurchase


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)
    recommended_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="ref_by"
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.code}"

    def get_recommended_profiles(self):
        qs = Profile.objects.all()
        my_recs = []
        for profile in qs:
            if profile.recommended_by == self.user:
                my_recs.append(profile)
        return my_recs

    # def get_recommended_profiles_with_machine(self):
    #     # Filter profiles based on recommended_by and machine purchase
    #     rs = Profile.objects.filter(recommended_by=self.user)
    #     purchased_profiles = MachinePurchase.objects.filter(user__profile__in=rs)
    #     return purchased_profiles
    def get_recommended_profiles_with_machine(self):
        # Get distinct users who own at least one machine
        recommended_profiles = (
            Profile.objects.filter(
                recommended_by=self.user, user__machinepurchase__isnull=False
            )
            .values("user__username")
            .distinct()
        )
        return recommended_profiles
    
    def get_recommended_profiles_with_machine_count(self):
        # Get distinct users who own at least one machine
        recommended_profiles_count = (
            Profile.objects.filter(
                recommended_by=self.user, user__machinepurchase__isnull=False
            )
            .values("user__username")
            .distinct().count()
        )
        return recommended_profiles_count

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)
