from income.models import Paycheck, Income
from monthly_bills.models import *
from .models import *
import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from daily_expenses.functions import *


# get all of last months paychecks plus all of this months including any future checks.
def get_paychecks_function(user):
    now = date.today()
    #now = now.replace(day=19, month=4)
    this_entire_month = abs(now.month + 1)
    this_entire_month = now.replace(month=this_entire_month, day=1)

    one_month_ago = now - relativedelta(months=+1)
    range1 = calendar.monthrange(one_month_ago.year, one_month_ago.month)
    last_day = range1[1]
    one_month_ago = now.replace(month=one_month_ago.month, day=last_day)

    paychecks = Paycheck.objects.filter(user_id=user,
                                        pay_date__gt=one_month_ago,
                                        pay_date__lt=this_entire_month).values()

    if len(paychecks) > 0:
        return paychecks
    else:
        paychecks = False
        return paychecks


#
def weekly_paycheck_create_function(user, date1, next_paycheck):

    try:
        Paycheck.objects.filter(user_id=user, pay_date__gte=next_paycheck).delete()
    except:
        pass

    income = Income.objects.get(user_id=user)
    total_frequency = int(income.frequency)
    till_next_paycheck = datetime.timedelta(days=0)

    for frequency in range(total_frequency):

        next_paycheck = next_paycheck + till_next_paycheck
        Paycheck.objects.create(user_id=user,
                                description=income.description,
                                amount=income.amount,
                                pay_date=next_paycheck)
        till_next_paycheck = datetime.timedelta(days=7)


#
def biweekly_paycheck_create_function(user, date1, next_paycheck):

    try:
        Paycheck.objects.filter(user_id=user, pay_date__gte=next_paycheck).delete()
    except:
        pass

    income = Income.objects.get(user_id=user)
    total_frequency = int(income.frequency)
    till_next_paycheck = datetime.timedelta(days=0)

    for frequency in range(total_frequency):

        next_paycheck = next_paycheck + till_next_paycheck
        Paycheck.objects.create(user_id=user,
                                description=income.description,
                                amount=income.amount,
                                pay_date=next_paycheck)
        till_next_paycheck = datetime.timedelta(days=14)


#
def bimonthly_paycheck_create_function(user, date1, next_paycheck):

    try:
        Paycheck.objects.filter(user_id=user, pay_date__gte=next_paycheck).delete()
    except:
        pass

    income = Income.objects.get(user_id=user)
    total_frequency = (int(income.frequency) / 2)
    next_paycheck1 = next_paycheck.replace(day=15)
    next_paycheck1 = next_paycheck1 + relativedelta(months=+1)
    for frequency in range(total_frequency):

        range1 = calendar.monthrange(next_paycheck.year, next_paycheck.month)
        last = range1[1]
        next_paycheck = next_paycheck.replace(day=last)

        Paycheck.objects.create(user_id=user,
                                description=income.description,
                                amount=income.amount,
                                pay_date=next_paycheck)
        next_paycheck = next_paycheck + relativedelta(months=+1)

        Paycheck.objects.create(user_id=user,
                                description=income.description,
                                amount=income.amount,
                                pay_date=next_paycheck1)
        next_paycheck1 = next_paycheck1 + relativedelta(months=+1)


#
def bimonthly_paycheck_create_function1(user, date1, next_paycheck):
    try:
        Paycheck.objects.filter(user_id=user, pay_date__gte=next_paycheck).delete()
    except:
        pass

    income = Income.objects.get(user_id=user)
    total_frequency = (int(income.frequency) / 2)
    next_paycheck1 = next_paycheck.replace(day=15)

    for frequency in range(total_frequency):

        Paycheck.objects.create(user_id=user,
                                description=income.description,
                                amount=income.amount,
                                pay_date=next_paycheck1)
        next_paycheck1 = next_paycheck1 + relativedelta(months=+1)

        range1 = calendar.monthrange(next_paycheck.year, next_paycheck.month)
        last = range1[1]
        next_paycheck = next_paycheck.replace(day=last)

        Paycheck.objects.create(user_id=user,
                                description=income.description,
                                amount=income.amount,
                                pay_date=next_paycheck)
        next_paycheck = next_paycheck + relativedelta(months=+1)


#
def monthly_paycheck_create_function(user, date1, next_paycheck):

    try:
        Paycheck.objects.filter(user_id=user, pay_date__gte=next_paycheck).delete()
    except:
        pass

    income = Income.objects.get(user_id=user)
    total_frequency = int(income.frequency)

    for frequency in range(total_frequency):

        Paycheck.objects.create(user_id=user,
                                description=income.description,
                                amount=income.amount,
                                pay_date=next_paycheck)
        next_paycheck = next_paycheck + relativedelta(months=+1)


#
def get_income_funtion(user):
    try:
        income = Income.objects.get(user_id=user)
    except:
        income = False

    return income


#
def get_frequency_function(user):

    try:
        income = Income.objects.get(user_id=user)
        if income.frequency == '52':
            var = "Weekly"
        elif income.frequency == '24':
            var = "Biweekly"
        elif income.frequency == '26':
            var = "Bimonthly"
        elif income.frequency == '12':
            var = "Monthly"

        return var

    except:
        pass


# Things to keep in mind here.  This function will calc the gap between paychecks for ALL paychecks.
# Remember, ALL PAYCHECKS and so you only really have to worry abou the first.
def till_next_paycheck_function(user, now):

    try:
        income = get_income_funtion(user)
        x = int(income.frequency)

        if x == 52:
            try:
                check = Paycheck.objects.filter(user_id=user).order_by("id")[0]
                now1 = check.pay_date - timedelta(days=7)                             # bug bug
                for check in Paycheck.objects.filter(user_id=user).order_by("-id"):
                    paycheck = Paycheck.objects.get(id=check.id)
                    gap = abs(now1 - check.pay_date)
                    paycheck.time_till_next = int(gap.days)
                    paycheck.save()
                    now1 = check.pay_date
            except:
                pass

        if x == 26:
            try:
                check = Paycheck.objects.filter(user_id=user).order_by("id")[0]
                now1 = check.pay_date - timedelta(days=14)                          # bug bug
                for check in Paycheck.objects.filter(user_id=user).order_by("-id"):
                    paycheck = Paycheck.objects.get(id=check.id)
                    gap = abs(now1 - check.pay_date)
                    paycheck.time_till_next = int(gap.days)
                    paycheck.save()
                    now1 = check.pay_date
            except:
                pass

        if x == 24:
            try:
                check = Paycheck.objects.filter(user_id=user).order_by("id")[0]
                if check.pay_date.day == 15:
                    now1 = check.pay_date - timedelta(days=15)                      # bug bug
                    for check in Paycheck.objects.filter(user_id=user).order_by("-id"):
                        paycheck = Paycheck.objects.get(id=check.id)
                        gap = abs(now1 - check.pay_date)
                        paycheck.time_till_next = int(gap.days)
                        paycheck.save()
                        now1 = check.pay_date

                range11 = calendar.monthrange(check.pay_date.year, check.pay_date.month)
                last_day = range11[1]
                if check.pay_date.day == last_day:
                    now1 = check.pay_date - timedelta(days=15)                              # bug bug
                    for check in Paycheck.objects.filter(user_id=user).order_by("-id"):
                        paycheck = Paycheck.objects.get(id=check.id)
                        gap = abs(now1 - check.pay_date)
                        paycheck.time_till_next = int(gap.days)
                        paycheck.save()
                        now1 = check.pay_date

            except:
                pass

        if x == 12:
            try:
                check = Paycheck.objects.filter(user_id=user).order_by("id")[0]
                now1 = check.pay_date - relativedelta(months=1)
                for check in Paycheck.objects.filter(user_id=user).order_by("-id"):
                    paycheck = Paycheck.objects.get(id=check.id)
                    gap = abs(now1 - check.pay_date)
                    paycheck.time_till_next = int(gap.days)
                    paycheck.save()
                    now1 = check.pay_date
            except:
                pass

    except:
        pass








