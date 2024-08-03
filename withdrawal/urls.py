from django.urls import path, include

# Create your tests here.
from .views import *

app_name = "withdrawal"

urlpatterns = [
    path('withdraw/',withdrawal,name="withdraw"),
    path('wrecord/',wrecord,name="wrecord")
]