from django.contrib import admin
from .models import Paycheck, Income


class PaycheckAdmin(admin.ModelAdmin):
    class Meta:
        model = Paycheck

admin.site.register(Paycheck, PaycheckAdmin)


class IncomeAdmin(admin.ModelAdmin):
    class Meta:
        model = Income

admin.site.register(Income, IncomeAdmin)



