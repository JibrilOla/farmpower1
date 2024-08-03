from django.shortcuts import render, redirect
from machine.models import MachinePurchase
from payments.models import UserWallet
from django.utils import timezone
from .models import ButtonClick
from registration.models import Profile
from .models import RecommendationsIncome


# Create your views here.
def earnbutton_click1(request):
    # Check if the user can click the button
    button_state, created = ButtonClick.objects.get_or_create(
        user=request.user, machine_name="A-1E2"
    )
    current_time = timezone.now()
    my_profile = Profile.objects.get(user=request.user)
    recommender = my_profile.recommended_by
    recommender_wallet = recommender.userwallet

    if (
        not button_state.clicked
        or current_time - button_state.last_clicked >= timezone.timedelta(days=1)
    ):
        button_state.clicked = True
        button_state.last_clicked = current_time
        button_state.save()
        if request.user.is_authenticated:
            user_wallet = UserWallet.objects.get(user=request.user)
            machines = MachinePurchase.objects.filter(
                user=request.user, machine_name="A-1E2"
            )
            for machine in machines:
                if machine.remaining_days > 0:
                    user_wallet.balance += 120
                    user_wallet.save()
                    recommender_wallet.balance += 12
                    recommender_wallet.save()
                    RecommendationsIncome.objects.create(
                        user=recommender_wallet.user, amount=12
                    )
                    machine.remaining_days -= 1
                    machine.total += 120
                    machine.save()
                else:
                    return render(request, "machines/expired.html")

            return render(request, "machines/success.html", {"income": "N120"})
        else:
            # Redirect to the login page if the user is not authenticated
            return redirect("/login")
    else:
        return render(request, "machines/recieved.html")


def earnbutton_click2(request):
    user_wallet = UserWallet.objects.get(user=request.user)

    # Check if the user can click the button
    button_state, created = ButtonClick.objects.get_or_create(
        user=request.user, machine_name="A2-1E4"
    )
    current_time = timezone.now()
    my_profile = Profile.objects.get(user=request.user)
    recommender = my_profile.recommended_by
    recommender_wallet = recommender.userwallet

    if (
        not button_state.clicked
        or current_time - button_state.last_clicked >= timezone.timedelta(days=1)
    ):
        button_state.clicked = True
        button_state.last_clicked = current_time
        button_state.save()
        if request.user.is_authenticated:
            machines = MachinePurchase.objects.filter(
                user=request.user, machine_name="A2-1E4"
            )
            for machine in machines:
                if machine.remaining_days > 0:
                    user_wallet.balance += 250
                    user_wallet.save()
                    recommender_wallet.balance += 25
                    recommender_wallet.save()
                    RecommendationsIncome.objects.create(
                        user=recommender_wallet.user, amount=25
                    )
                    machine.remaining_days -= 1
                    machine.total += 250
                    machine.save()
                else:
                    return render(request, "machines/expired.html")

            return render(request, "machines/success.html", {"income": "N250"})
        else:
            # Redirect to the login page if the user is not authenticated
            return redirect("/login")
    else:
        return render(request, "machines/recieved.html")


def earnbutton_click3(request):
    # Check if the user can click the button
    button_state, created = ButtonClick.objects.get_or_create(
        user=request.user, machine_name="A-2E2"
    )
    current_time = timezone.now()

    my_profile = Profile.objects.get(user=request.user)
    recommender = my_profile.recommended_by
    recommender_wallet = recommender.userwallet

    if (
        not button_state.clicked
        or current_time - button_state.last_clicked >= timezone.timedelta(days=1)
    ):
        button_state.clicked = True
        button_state.last_clicked = current_time
        button_state.save()
        if request.user.is_authenticated:
            user_wallet = UserWallet.objects.get(user=request.user)
            machines = MachinePurchase.objects.filter(
                user=request.user, machine_name="A-2E2"
            )
            for machine in machines:
                if machine.remaining_days > 0:
                    user_wallet.balance += 540
                    user_wallet.save()
                    recommender_wallet.balance += 54
                    recommender_wallet.save()
                    RecommendationsIncome.objects.create(
                        user=recommender_wallet.user, amount=54
                    )
                    machine.remaining_days -= 1
                    machine.total += 540
                    machine.save()
                else:
                    return render(request, "machines/expired.html")

            return render(request, "machines/success.html", {"income": "N540"})
        else:
            return redirect("/login")
    else:
        return render(request, "machines/recieved.html")


def earnbutton_click4(request):
    # Check if the user can click the button
    button_state, created = ButtonClick.objects.get_or_create(
        user=request.user, machine_name="PW2-E20"
    )
    current_time = timezone.now()
    my_profile = Profile.objects.get(user=request.user)
    recommender = my_profile.recommended_by
    recommender_wallet = recommender.userwallet

    if (
        not button_state.clicked
        or current_time - button_state.last_clicked >= timezone.timedelta(days=1)
    ):
        button_state.clicked = True
        button_state.last_clicked = current_time
        button_state.save()
        if request.user.is_authenticated:
            user_wallet = UserWallet.objects.get(user=request.user)
            machines = MachinePurchase.objects.filter(
                user=request.user, machine_name="PW2-E20"
            )
            for machine in machines:
                if machine.remaining_days > 0:
                    user_wallet.balance += 950
                    user_wallet.save()
                    recommender_wallet.balance += 95
                    recommender_wallet.save()
                    RecommendationsIncome.objects.create(
                        user=recommender_wallet.user, amount=95
                    )
                    machine.remaining_days -= 1
                    machine.total += 950
                    machine.save()
                else:
                    return render(request, "machines/expired.html.html")

            return render(request, "machines/success.html", {"income": "N950"})
        else:
            # Redirect to the login page if the user is not authenticated
            return redirect("/login")
    else:
        return render(request, "machines/recieved.html")


def earnbutton_click5(request):
    # Check if the user can click the button
    button_state, created = ButtonClick.objects.get_or_create(
        user=request.user, machine_name="A2-A20"
    )
    current_time = timezone.now()
    my_profile = Profile.objects.get(user=request.user)
    recommender = my_profile.recommended_by
    recommender_wallet = recommender.userwallet

    if (
        not button_state.clicked
        or current_time - button_state.last_clicked >= timezone.timedelta(days=1)
    ):
        button_state.clicked = True
        button_state.last_clicked = current_time
        button_state.save()
        if request.user.is_authenticated:
            user_wallet = UserWallet.objects.get(user=request.user)
            machines = MachinePurchase.objects.filter(
                user=request.user,
                machine_name="A2-A20",
            )
            for machine in machines:
                if machine.remaining_days > 0:
                    user_wallet.balance += 1830
                    user_wallet.save()
                    recommender_wallet.balance += 183
                    recommender_wallet.save()
                    RecommendationsIncome.objects.create(
                        user=recommender_wallet.user, amount=183
                    )
                    machine.remaining_days -= 1
                    machine.total += 1830

                    machine.save()
                else:
                    return render(request, "machines/expired.html.html")

            return render(request, "machines/success.html", {"income": "N1830"})
        else:
            # Redirect to the login page if the user is not authenticated
            return redirect("/login")
    else:
        return render(request, "machines/recieved.html")


def ref_income(request):
    if request.user.is_authenticated:
        ref_income = RecommendationsIncome.objects.filter(user=request.user)
        con = {"ref_income": ref_income}
        return render(request, "records/ref_income.html", con)
    else:
        return redirect("/login")
