from django.db import models
from django.contrib.auth.models import User


class Paycheck(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=30)
    amount = models.CommaSeparatedIntegerField(max_length=10)
    pay_date = models.DateField(null=True)
    time_till_next = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, blank=True, null=True)

    class Meta:
        ordering = ['pay_date']

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.description,
                                    self.amount,
                                    self.pay_date,
                                    self.id,
                                    self.time_till_next)


class Income(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    FREQUENCY = (
        ('12', 'Monthly'),
        ('24', '15th and last-day-of-month'),
        ('26', 'Bi-weekly'),
        ('52', 'Weekly'),
    )

    frequency = models.CharField(max_length=200, choices=FREQUENCY)
    next_paycheck = models.DateField()

    def __unicode__(self):
        return u'%s %s %s %s' % (self.description,
                                 self.amount,
                                 self.frequency,
                                 self.next_paycheck)



