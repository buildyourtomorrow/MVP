from django import forms
from .models import Paycheck, Income
from django.forms.extras.widgets import SelectDateWidget


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ['description', 'frequency', 'amount', 'next_paycheck']
        widgets = {'next_paycheck': forms.DateInput(attrs={'class': 'datepicker'})}


class IncomeEditForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ['description', 'frequency', 'amount', 'next_paycheck']
        widgets = {'next_paycheck': forms.DateInput(attrs={'class': 'datepicker'})}


class PaycheckEditForm(forms.ModelForm):

    class Meta:
        model = Paycheck
        fields = ['description', 'amount', 'pay_date']
        widgets = {'pay_date': forms.DateInput(attrs={'class': 'datepicker'})}


