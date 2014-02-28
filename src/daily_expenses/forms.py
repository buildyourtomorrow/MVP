from django import forms
from .models import DailyExpense, Cash, DatePicker
from django.forms.extras.widgets import SelectDateWidget


class DailyExpenseForm(forms.ModelForm):

    class Meta:
        model = DailyExpense
        fields = ['description', 'date', 'amount']
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}


class EditExpenseForm(forms.ModelForm):

    class Meta:
        model = DailyExpense
        fields = ['description', 'amount', 'date']
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}


class DatePickerForm(forms.ModelForm):

    class Meta:
        model = DatePicker
        fields = ['date']
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}


