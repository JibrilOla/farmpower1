from django.urls import path
from .views import * 
app_name="payments"
urlpatterns = [
	path('initiate-payment/',initiate_payment, name='initiate_payment'),
	path('verify_payment/<str:ref>',verifypayment, name='verifypayment'),
    path('rechargerecord/',rechargerec,name='rechargerec'),
]