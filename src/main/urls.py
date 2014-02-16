from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.landing_page', name='landing_pages'),
    url(r'^income/', include('income.urls')),
    url(r'^daily_budget/', include('daily_expenses.urls')),
    url(r'^accounts/profile/$', 'income.views.dashboard11'),
    url(r'^accounts/activate/complete/$', 'income.views.dashboard12'),

    #override the default urls
    url(r'^password/change/$',
        auth_views.password_change,
        name='password_change'),

    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),

    url(r'^password/reset/$',
        auth_views.password_reset,
        name='password_reset'),

    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),

    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),

    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),

    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'', include('registration.backends.default.urls')),
    url(r'^bills/', include('monthly_bills.urls')),
    url(r'^admin/', include(admin.site.urls)),
)




