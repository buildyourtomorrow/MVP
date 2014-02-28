from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('daily_expenses.views',
    url(r'^$', 'dashboard', name='dashboard'),
    url(r'^expense$', 'expense', name='expense'),
    url(r'^datepicker$', 'datepicker', name='datepicker'),
    url(r'^expense_delete/(?P<id>\d+)$', 'delete', name='transaction_delete'),
    url(r'^edit_expense/(?P<id>\d+)', 'edit_expense', name='edit_expense'),
)

