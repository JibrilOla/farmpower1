from django.urls import path
from .views import *

app_name = "income"
urlpatterns = [
    path("receive/120.00/", earnbutton_click1, name="button"),
    path("receive/250.00/", earnbutton_click2, name="button"),
    path("receive/540.00/", earnbutton_click3, name="button"),
    path("receive/950.00/", earnbutton_click4, name="button"),
    path("receive/1830.00/", earnbutton_click5, name="button"),
    path("ref-income/",ref_income,name="ref_income")
]
