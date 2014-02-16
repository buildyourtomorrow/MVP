from django import forms
from .models import Paycheck, Income
from django.forms.extras.widgets import SelectDateWidget


class IncomeForm(forms.ModelForm):
    next_paycheck = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Income
        fields = ['description', 'frequency', 'amount', 'next_paycheck']


class IncomeEditForm(forms.ModelForm):
    start_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Income
        fields = ['description', 'frequency', 'amount']


class PaycheckEditForm(forms.ModelForm):
    pay_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Paycheck
        fields = ['description', 'amount', 'pay_date']





