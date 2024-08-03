from django.shortcuts import render, redirect
from .models import Payment, UserWallet
from django.conf import settings
from django.contrib.auth.decorators import login_required


def initiate_payment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            amount = request.POST["amount"]
            email = request.POST["email"]
            pk = settings.PAYSTACK_PUBLIC_KEY

            payment = Payment.objects.create(
                amount=amount, email=email, user=request.user
            )
            if int(payment.amount) >= 2000:
                payment.save()

                context = {
                    "payment": payment,
                    "field_values": request.POST,
                    "paystack_pub_key": pk,
                    "amount_value": payment.amount_value(),
                }
                return render(request, "payments/make_payment.html", context)
            else:
                error_message = (
                    "Minimum recharge is 2000. Please enter a correct recharge amount."
                )
                return render(
                    request, "payments/recharge.html", {"error_message": error_message}
                )

        return render(request, "payments/recharge.html")
    else:
        return redirect("/login")


def verifypayment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verifypayment()

    if verified:
        payment.verified = True
        user_wallet = UserWallet.objects.get(user=request.user)
        user_wallet.balance = user_wallet.balance + payment.amount
        user_wallet.save()
        print(request.user.username, " funded wallet successfully")
        return render(request, "payments/success.html")

    return render(request, "payments/success.html")


@login_required
def rechargerec(request):
    rec = Payment.objects.filter(user=request.user, verified=True).order_by(
        "-date_created"
    )
    data = {"rec": rec}
    return render(request, "records/recharge_rec.html", data)
