from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('income.views',
    url(r'^$', 'dashboard', name='income_dashboard'),
    url(r'^add$', 'add', name='add'),
    url(r'^edit/(?P<u>\d+)/$', 'paycheck_edit', name='paycheck_edit'),
    url(r'^delete/(?P<u>\d+)/$', 'delete', name='income_delete'),
    url(r'^income_edit/(?P<u>\d+)/$', 'income_edit', name='income_edit'),
    url(r'^frequency$', 'frequency', name='frequency'),
    url(r'^delete_income/$', 'delete_income', name='delete_income'),
)


