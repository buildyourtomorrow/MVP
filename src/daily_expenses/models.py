from django.db import models
from django.contrib.auth.models import User


class DailyExpense(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()
    description = models.CharField(max_length=200)
    to_transaction_sum = models.DecimalField(max_digits=15, decimal_places=8, default=0.00, blank=True)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.user, self.amount, self.date, self.description, self.to_transaction_sum)


class TotalDailyExpenses(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.amount, self.date)


class BeginningDailyBudget(models.Model):
    user = models.ForeignKey(User)
    beginning_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.beginning_amount, self.date)


class EndingDailyBudget(models.Model):
    user = models.ForeignKey(User)
    ending_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.beginning_amount, self.date)


class BeginningPeriodBudget(models.Model):
    user = models.ForeignKey(User)
    beginning_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.beginning_amount, self.date)


class EndingPeriodBudget(models.Model):
    user = models.ForeignKey(User)
    ending_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.ending_amount, self.date)


class Cash(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.amount, self.date)


class PeriodBudget(models.Model):
    user = models.ForeignKey(User)
    beginning_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    ending_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s %s' % (self.user, self.beginning_amount, self.ending_amount, self.date)


class DailyBudget(models.Model):
    user = models.ForeignKey(User)
    beginning_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    ending_amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s %s' % (self.user, self.beginning_amount, self.ending_amount, self.date)


class PeriodExpense(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.amount, self.date)


class Transaction(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    daily_budget = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    period_budget = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)
    date = models.DateField()
    daily_expense_id = models.DecimalField(max_digits=15, decimal_places=8, default=0.00)

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.amount, self.date)


class DatePicker(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.user, self.date)







