from django.contrib import admin
from .models import Paycheck


class PaycheckAdmin(admin.ModelAdmin):
    class Meta:
        model = Paycheck

admin.site.register(Paycheck, PaycheckAdmin)



