from .forms import WithdrawalForm
from .models import Withdrawal

from django.shortcuts import render, redirect
from payments.models import UserWallet
from machine.models import MachinePurchase


def withdrawal(request):
    if request.user.is_authenticated:
        user_wallet = UserWallet.objects.get(user=request.user)
        if MachinePurchase.objects.filter(user=request.user).exists():
            if request.method == "POST":
                form = WithdrawalForm(request.POST)
                withdrawal_amount = float(request.POST.get("withdrawal_amount"))

                if withdrawal_amount >= 1000:
                    if withdrawal_amount <= user_wallet.balance:
                        if form.is_valid():
                            withdrawal = form.save(commit=False)
                            withdrawal.user = request.user
                            user_wallet.balance -= withdrawal_amount
                            withdrawal.save()
                            user_wallet.save()
                            return redirect("/wrecord")
                    else:
                        error_message = "Insufficient balance.Please enter amount within balance range!"
                        return render(
                            request,
                            "payments/withdraw.html",
                            {"error_message": error_message},
                        )
                else:
                    error_message = "Minimum withdrawal is 1000. Please enter a higher withdrawal amount."
                    return render(
                        request,
                        "payments/withdraw.html",
                        {"error_message": error_message},
                    )

            else:
                form = WithdrawalForm()
                return render(
                    request,
                    "payments/withdraw.html",
                    {"form": form, "balance": user_wallet.balance},
                )
        else:
            error_message = "You have not purchased a machine. Please purchase a machine to activate withdrawal."
            return render(
                request, "payments/withdraw.html", {"error_message": error_message}
            )
    else:
        return redirect("/login")


def wrecord(request):
    if request.user.is_authenticated:
        withdrawals = Withdrawal.objects.filter(user=request.user).order_by(
            "-date_placed"
        )
        return render(
            request, "records/withdraw_rec.html", {"withdrawals": withdrawals}
        )
    else:
        return redirect("/login")
