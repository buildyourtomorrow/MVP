from django.contrib import admin
from .models import *


class DailyExpenseAdmin(admin.ModelAdmin):
    class Meta:
        model = DailyExpense

admin.site.register(DailyExpense, DailyExpenseAdmin)


class TotalDailyExpensesAdmin(admin.ModelAdmin):
    class Meta:
        model = TotalDailyExpenses

admin.site.register(TotalDailyExpenses, TotalDailyExpensesAdmin)


class BeginningDailyBudgetAdmin(admin.ModelAdmin):
    class Meta:
        model = BeginningDailyBudget

admin.site.register(BeginningDailyBudget, BeginningDailyBudgetAdmin)


class EndingDailyBudgetAdmin(admin.ModelAdmin):
    class Meta:
        model = EndingDailyBudget

admin.site.register(EndingDailyBudget, EndingDailyBudgetAdmin)


class BeginningPeriodBudgetAdmin(admin.ModelAdmin):
    class Meta:
        model = BeginningPeriodBudget

admin.site.register(BeginningPeriodBudget, BeginningPeriodBudgetAdmin)


class EndingPeriodBudgetAdmin(admin.ModelAdmin):
    class Meta:
        model = EndingPeriodBudget

admin.site.register(EndingPeriodBudget, EndingPeriodBudgetAdmin)


class PeriodBudgetAdmin(admin.ModelAdmin):
    class Meta:
        model = PeriodBudget

admin.site.register(PeriodBudget, PeriodBudgetAdmin)


class DailyBudgetAdmin(admin.ModelAdmin):
    class Meta:
        model = DailyBudget

admin.site.register(DailyBudget, DailyBudgetAdmin)


class PeriodExpenseAdmin(admin.ModelAdmin):
    class Meta:
        model = PeriodExpense

admin.site.register(PeriodExpense, PeriodExpenseAdmin)


class TransactionAdmin(admin.ModelAdmin):
    class Meta:
        model = Transaction

admin.site.register(Transaction, TransactionAdmin)


class DatePickerAdmin(admin.ModelAdmin):
    class Meta:
        model = DatePicker

admin.site.register(DatePicker, DatePickerAdmin)