from django import forms
from .models import Withdrawal

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['withdrawal_amount', 'account_holder_name', 'account_number', 'bank_name']
