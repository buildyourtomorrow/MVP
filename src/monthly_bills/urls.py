from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('monthly_bills.views',
    url(r'^$', 'dashboard', name='bills_dashboard'),
    url(r'^add$', 'add', name='bills_add'),
    url(r'^edit/(?P<u>\d+)/$', 'edit', name='monthly_bill_edit'),
    url(r'^delete/(?P<u>\d+)/$', 'delete', name='monthly_delete'),
)
