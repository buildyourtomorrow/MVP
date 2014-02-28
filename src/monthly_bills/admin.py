from django.contrib import admin
from .models import *


class BillAdmin(admin.ModelAdmin):
    class Meta:
        model = Bill

admin.site.register(Bill, BillAdmin)


class BillTotalAdmin(admin.ModelAdmin):
    class Meta:
        model = BillTotal

admin.site.register(BillTotal, BillTotalAdmin)


