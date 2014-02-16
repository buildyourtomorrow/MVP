from django import forms
from .models import DailyExpense, Cash, DatePicker
from django.forms.extras.widgets import SelectDateWidget


class DailyExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = DailyExpense
        fields = ['description', 'date', 'amount']


class CashForm(forms.ModelForm):
    pay_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Cash
        fields = ['amount', 'date']


class EditExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = DailyExpense
        fields = ['description', 'amount', 'date']


class DatePickerForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = DatePicker
        fields = ['date']




