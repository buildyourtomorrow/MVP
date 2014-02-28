from django.db import models
from django.contrib.auth.models import User


class Bill(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, default=0.00, decimal_places=0)

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.description, self.amount)


class BillTotal(models.Model):
    user = models.ForeignKey(User)
    monthly_total = models.DecimalField(max_digits=10, default=0.00, decimal_places=0)
    weekly = models.DecimalField(max_digits=10, default=0.00, decimal_places=0)
    daily = models.DecimalField(max_digits=10, default=0.00, decimal_places=0)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.user, self.monthly_total, self.weekly, self.daily)

