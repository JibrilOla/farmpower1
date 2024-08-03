from django.shortcuts import render, redirect

# Create your views here.
from .models import MachinePurchase
from payments.models import UserWallet
from django.utils import timezone
from datetime import timedelta
from django.db.models import F


def select_machine(request, price, income, name):
    if request.user.is_authenticated:
        data = {"price": price, "name": name, "income": income}
        return render(request, "machines/purchase.html", data)
    else:
        return redirect("/login")


def purchase_machine(request, price, name, income):
    if request.user.is_authenticated:
        existing_machine = MachinePurchase.objects.filter(
            user=request.user, machine_name=name, remaining_days__gte=1
        ).first()
        expired_machine = MachinePurchase.objects.filter(
            user=request.user, machine_name=name, remaining_days__lt=1
        ).first()

        if existing_machine:
            return render(
                request,
                "payments/failed.html",
                {
                    "error_message": "You currently own this machine and cannot purchase it again till it expires"
                },
            )
        user_wallet = UserWallet.objects.get(user=request.user)
        if user_wallet.balance >= price:
            user_wallet.balance -= price
            user_wallet.save()
            if expired_machine:
                expired_machine.delete()
            income = income
            machine = MachinePurchase.objects.create(
                user=request.user,
                machine_name=name,
                price=price,
                is_verified=True,
                income=income,
                remaining_days=30,
            )
            machine.save()

            return render(request, "payments/success.html")
        else:
            return render(request, "payments/failed.html")
    else:
        return redirect("/login")


def mymachine(request):
    if request.user.is_authenticated:
        mymachine = MachinePurchase.objects.filter(user=request.user).order_by(
            "-purchase_date"
        )
        data = {"mymachine": mymachine}
        return render(request, "machines/mymachine.html", data)
    else:
        return redirect("/login")


def button(request):
    return render(request, "machines/mymachine.html")


def ttincome(request):
    mymachine = MachinePurchase.objects.filter(user=request.user)
    return render(request, "machines/machineincome.html", {"mymachine": mymachine})
