from django.shortcuts import render, redirect
from registration.models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from payments.models import UserWallet
from django.contrib import messages
from machine.models import MachinePurchase
from payments.models import Payment
from withdrawal.models import Withdrawal
from income.models import RecommendationsIncome

def Register(request, *args, **kwargs):
    code = str(kwargs.get("ref_code"))
    if code:
        profile = Profile.objects.get(code=code)
        request.session["ref_profile"] = profile.id
        print("id", profile.id)
        profile_id = request.session.get("ref_profile")
        print("profile_id", profile_id)
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            if profile_id is not None:
                recommended_by_profile = Profile.objects.get(id=profile_id)

                instance = form.save()
                registered_user = User.objects.get(id=instance.id)
                registered_profile = Profile.objects.get(user=registered_user)
                registered_profile.recommended_by = recommended_by_profile.user
                registered_profile.save()
            else:
                messages.error(request, "Get a valid ref link!!")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/login")
    else:
        return redirect("/register")
    context = {"form": form, "code": code}
    return render(request, "registration/register.html", context)


def Login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        userx = authenticate(request, username=user, password=password)
        if userx is not None:
            login(request, userx)
            return redirect("/home")
        else:
            return redirect("/login")
    return render(request, "registration/logins.html")


def my_recommendations_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        rcode = Profile.objects.get(user=request.user)
        refcode = rcode.code
        my_recs = profile.get_recommended_profiles
        purchased_profiles= profile.get_recommended_profiles_with_machine
        purchased_profiles_count= profile.get_recommended_profiles_with_machine_count()

        domain = request.get_host
        user = request.user
        my_profile = user.profile
        trecommended_profiles = my_profile.get_recommended_profiles()
        recommended_users = [profile.user for profile in trecommended_profiles]
        trecommended_revenue = (
            MachinePurchase.objects.filter(user__in=recommended_users)
            .aggregate(Sum("price", default=0))
            .get("price__sum", 0.00)
        )
        num_recs=len(recommended_users)

        recommendations_income_records = RecommendationsIncome.objects.filter(user=request.user)

        # Calculate total amount
        total_recommendations_income = recommendations_income_records.aggregate(Sum('amount'))['amount__sum'] or 0



        context = {
            "my_recs": my_recs,
            "my_recs2": purchased_profiles,
            "refcode": refcode,
            "domain": domain,
            "ptitle": "Team",
            "trecommended_revenue": trecommended_revenue,
            "num_recs":num_recs,
            "num_recs2":purchased_profiles_count,
            "tincome":total_recommendations_income 
        }
        return render(request, "sitepages/team.html", context)

    else:
        return redirect("/login")


from django.db.models import Sum


def Dashboard(request):
    if request.user.is_authenticated:
        # Get the total income of each machine type that the user owns
        total_a1e2 = (
            MachinePurchase.objects.filter(
                machine_name="A-1E2", user=request.user
            ).aggregate(Sum("total"))["total__sum"]
            or 0
        )
        total_a21e4 = (
            MachinePurchase.objects.filter(
                machine_name="A2-1E4", user=request.user
            ).aggregate(Sum("total"))["total__sum"]
            or 0
        )
        total_a2e2 = (
            MachinePurchase.objects.filter(
                machine_name="A-2E2", user=request.user
            ).aggregate(Sum("total"))["total__sum"]
            or 0
        )
        total_pw2e20 = (
            MachinePurchase.objects.filter(
                machine_name="PW2-E20", user=request.user
            ).aggregate(Sum("total"))["total__sum"]
            or 0
        )
        total_a2a20 = (
            MachinePurchase.objects.filter(
                machine_name="A2-A20", user=request.user
            ).aggregate(Sum("total"))["total__sum"]
            or 0
        )

        # Add them up to get the overall total
        total_income = (
            total_a1e2 + total_a21e4 + total_a2e2 + total_pw2e20 + total_a2a20
        )

        # Get the total verified payment for each user
        total_verified_payment = (
            Payment.objects.filter(verified=True, user=request.user)
            .aggregate(Sum("amount", default=0))
            .get("amount__sum", 0.00)
        )

        # Get the total amount of all the machines bought by the user
        total_revenue = (
            MachinePurchase.objects.filter(user=request.user)
            .aggregate(Sum("price", default=0))
            .get("price__sum", 0.00)
        )

        # Get the total withdrawal amount by each user
        total_withdrawn = (
            Withdrawal.objects.filter(user=request.user)
            .aggregate(Sum("withdrawal_amount", default=0))
            .get("withdrawal_amount__sum", 0.00)
        )

        user_wallet = UserWallet.objects.get(user=request.user)
        data = {
            "ptitle": "User Dashboard",
            "balance": user_wallet.balance,
            "total_income": total_income,
            "total_recharge": total_verified_payment,
            "total_revenue": total_revenue,
            "total_withdrawn": total_withdrawn,
        }
        return render(request, "sitepages/dashboard.html", data)
    else:
        return redirect("/login")
