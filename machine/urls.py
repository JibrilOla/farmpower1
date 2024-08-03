from django.urls import path
from .views import *

app_name = "machines"
urlpatterns = [
    path(
        "select/<str:name>/<int:price>/<int:income>",
        select_machine,
        name="purchase_machine",
    ),
    path(
        "purchase/<int:price>/<int:income>/<str:name>",
        purchase_machine,
        name="purchase_machine",
    ),
    path("mymachine/", mymachine, name="mymachine"),
    path("ttincome/", ttincome, name="ttincome"),
]
