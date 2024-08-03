from django.urls import path, include

# Create your tests here.
from .views import *

app_name = "sitepages"

urlpatterns = [
    path("home/", Home, name="home"),
    # path("logins/", logins, name="logins"),
    path("", Home, name="home"),
    path("products/", Products, name="products"),
    path("", include("django.contrib.auth.urls")),
    # records
    path("customerservice/", customer_service, name="customer_service"),
    path("passwordreset/", password_reset, name="password_reset"),
    path("help/", infohelp, name="help"),
]
