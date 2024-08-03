from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from payments.models import UserWallet, Payment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def Home(request):
    return render(request, "sitepages/home.html")


def Products(request):
    if request.user.is_authenticated:
        data = {"ptitle": "Machines"}
        return render(request, "sitepages/products.html", data)
    else:
        return redirect("/login")


# RECORD
def infohelp(request):
    if request.user.is_authenticated:
        return render(request, "sitepages/help.html")
    else:
        return redirect("/login")


def customer_service(request):
    return render(request, "records/customer_service.html")


def password_reset(request):
    return render(request, "records/password_reset.html")


# def logins(request):
#     return render(request,"registration/logins.html")
