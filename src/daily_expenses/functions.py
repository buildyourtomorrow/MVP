from monthly_bills.models import Bill, BillTotal
from income.models import Income, Paycheck
from .models import *
import datetime
from datetime import date
from datetime import timedelta


# calculates the daily budget or annual income minus annual bills expenses divided by 365
def daily_budget_function(user, now):

    paycheck = Paycheck.objects.filter(user_id=user, pay_date__lte=now).order_by("-id")[0]
    bills = BillTotal.objects.get(user_id=user)
    amount = float(paycheck.amount)
    time_till_next = float(paycheck.time_till_next)
    if time_till_next == 0:
        time_till_next = Paycheck.objects.filter(user_id=user, pay_date__gte=now).order_by("id")[1]
        time_till_next = float(time_till_next.time_till_next)
    else:
        pass
    monthly_bill_total = float(bills.monthly_total)
    paycheck1 = Paycheck.objects.filter(user_id=user)
    num_of_paychecks = len(paycheck1)
    daily_budget = float(amount / time_till_next) - (((monthly_bill_total * 12) / num_of_paychecks) / time_till_next)

    try:
        x = EndingPeriodBudget.objects.filter(user_id=user, date__lt=now).order_by("-id")[0]
        if x.ending_amount < 0:
            daily_budget = 0
    except:
        pass

    return daily_budget


# calculates the weekly budget or annual income minus annual bills expenses divided by 52
def period_budget_function(user, now):
    income = Income.objects.get(user_id=user)
    paycheck = Paycheck.objects.filter(user_id=user, pay_date__lte=now).order_by("-id")[0]
    bills = BillTotal.objects.get(user_id=user)
    amount = float(paycheck.amount)
    monthly_bill_total = float(bills.monthly_total)
    income.frequency = float(income.frequency)
    paycheck = Paycheck.objects.filter(user_id=user)
    num_of_paychecks = len(paycheck)
    period_budget = float(amount - ((monthly_bill_total * 12) / num_of_paychecks))
    return period_budget


# calculates the sum of all daily expenses.
def total_daily_expenses_function(user, date1):
    expenses = DailyExpense.objects.filter(user_id=user, date=date1).values()

    if len(expenses) > 0:
        var = 0
        for expense in expenses:
            var = var + expense['amount']

            TotalDailyExpenses.objects.filter(user_id=user, date=date1).delete()
            TotalDailyExpenses.objects.create(user_id=user,
                                              date=date1,
                                              amount=var)

        total = TotalDailyExpenses.objects.get(user_id=user, date=date1)
        return total.amount
    else:

        TotalDailyExpenses.objects.filter(user_id=user, date=date1).delete()
        TotalDailyExpenses.objects.create(user_id=user,
                                          date=date1,
                                          amount=0)
        total = TotalDailyExpenses.objects.get(user_id=user, date=date1)

        return total.amount


# calculates only the beginning daily budget - No more.
def beginning_daily_budget_function(user, date1):

    try:
        object11 = EndingDailyBudget.objects.filter(user_id=user, date__lt=date1).order_by("-id")[0]
        beginning_balance = float(object11.ending_amount) + float(daily_budget_function(user, date1))
        BeginningDailyBudget.objects.filter(user_id=user, date=date1).delete()

        BeginningDailyBudget.objects.create(user_id=user,
                                            date=date1,
                                            beginning_amount=beginning_balance)

        beginning_balance = BeginningDailyBudget.objects.get(user_id=user, date=date1)
        return beginning_balance

    except:
        BeginningDailyBudget.objects.filter(user_id=user, date=date1).delete()
        BeginningDailyBudget.objects.create(user_id=user,
                                            date=date1,
                                            beginning_amount=daily_budget_function(user, date1))

        beginning_balance = BeginningDailyBudget.objects.get(user_id=user, date=date1)
        return beginning_balance


#cals da ending budget. Example.  User starts with 50, spends 15, the user finishes with 35.  This function shld give 35.
def ending_daily_budget_function(user, date1):
    object1 = BeginningDailyBudget.objects.get(user_id=user,
                                               date=date1)
    EndingDailyBudget.objects.filter(user_id=user,
                                     date=date1).delete()
    ending_daily_budget = float(object1.beginning_amount + total_daily_expenses_function(user, date1))
    EndingDailyBudget.objects.create(user_id=user,
                                     date=date1,
                                     ending_amount=ending_daily_budget)
    ending_daily_budget = EndingDailyBudget.objects.get(user_id=user,
                                                        date=date1)
    return ending_daily_budget


# calculates only the beginning period budget - No more. Yesterday ending period is now beginning period for that day.
def beginning_period_budget_function(user, date1):
    try:
        beginning_period_balance = EndingPeriodBudget.objects.filter(user_id=user, date__lt=date1).order_by('-id')[0]
        BeginningPeriodBudget.objects.filter(user_id=user, date=date1).delete()
        beginning_period_balance = float(beginning_period_balance.ending_amount) + period_budget_add(user, date1)
        BeginningPeriodBudget.objects.create(user_id=user,
                                             date=date1,
                                             beginning_amount=beginning_period_balance)
        beginning_period_balance = BeginningPeriodBudget.objects.filter(user_id=user, date=date1).order_by("-id")[0]
        return beginning_period_balance
    except:
        BeginningPeriodBudget.objects.filter(user_id=user, date=date1).delete()
        BeginningPeriodBudget.objects.create(user_id=user,
                                             date=date1,
                                             beginning_amount=period_budget_function(user, date1))
        beginning_period_balance = BeginningPeriodBudget.objects.filter(user_id=user, date=date1).order_by("-id")[0]
        return beginning_period_balance


# calcs the ending period balance for a certain date. Ex. start the day with 200 for the week/period, 35 spent, 165 lft.
def ending_period_budget_function(user, date1):

        beginning_period_balance = BeginningPeriodBudget.objects.get(user_id=user, date=date1)
        ending_period_balance = beginning_period_balance.beginning_amount + total_daily_expenses_function(user, date1)
        EndingPeriodBudget.objects.filter(user_id=user, date=date1).delete()
        EndingPeriodBudget.objects.create(user_id=user,
                                          date=date1,
                                          ending_amount=ending_period_balance)
        ending_period_balance = EndingPeriodBudget.objects.filter(user_id=user, date=date1).order_by("-id")[0]
        return ending_period_balance


#
def create_transaction_function(user, date1):

    daily_expenses = DailyExpense.objects.filter(user_id=user, date=date1).values()
    Transaction.objects.filter(user_id=user, date=date1).delete()
    beginning_daily_balance = get_beginning_daily_budget(user, date1)
    beginning_period_balance = get_beginning_period_budget(user, date1)

    for expense in daily_expenses:

        Transaction.objects.create(user_id=user,
                                   amount=expense['amount'],
                                   description=expense['description'],
                                   daily_budget=beginning_daily_balance.beginning_amount + expense['to_transaction_sum'],
                                   period_budget=beginning_period_balance.beginning_amount + expense['to_transaction_sum'],
                                   date=date1,
                                   daily_expense_id=expense['id'])
    transactions = Transaction.objects.filter(user_id=user, date=date1)
    return transactions


#
def daily_expense_sum_to_transaction(user, date1):

    daily_expenses = DailyExpense.objects.filter(user_id=user, date=date1).values()

    var = 0
    for expense in daily_expenses:
        var = var + expense['amount']
        object1 = DailyExpense.objects.get(id=expense['id'])
        object1.to_transaction_sum = var
        object1.save()
    return var


#
def get_transactions(user, date1):
    transactions = Transaction.objects.filter(user_id=user,
                                              date=date1)
    return transactions


#
def get_beginning_daily_budget(user, date1):
    beginning_daily_budget = BeginningDailyBudget.objects.get(user_id=user,
                                                              date=date1)
    return beginning_daily_budget


#
def get_beginning_period_budget(user, date1):
    beginning_period_budget = BeginningPeriodBudget.objects.get(user_id=user,
                                                                date=date1)
    return beginning_period_budget


#
def update_daily_period_budget_function(user, date1):
    try:
        last_daily_ending_balance = EndingDailyBudget.objects.filter(user_id=user, date__lt=date1).order_by("-id")[0]
        last = last_daily_ending_balance.date
        gap = last - date1
        gap = abs(gap.days)
        if gap > 1:
            for day in range(gap):
                date2 = last + datetime.timedelta(days=1)
                beginning_daily_budget_function(user, date2)
                ending_daily_budget_function(user, date2)
                beginning_period_budget_function(user, date2)
                ending_period_budget_function(user, date2)
                last = date2
    except:
        pass


# gets the paycheck that is either greater than or equal to today's date.
def get_very_next_paycheck(user, date1):
    next_paycheck = Paycheck.objects.filter(user_id=user, pay_date__gt=date1).order_by("id")[0]
    next_paycheck = next_paycheck.pay_date - timedelta(days=1)
    return next_paycheck


def period_budget_add(user, date1):
    paycheck = Paycheck.objects.filter(user_id=user, pay_date__gte=date1).order_by("id")[0]
    if date1 == paycheck.pay_date:
        x = period_budget_function(user, date1)
        return x
    else:
        x = 0
        return x


#
def get_all_paychecks_to_show(user, date1):
    try:
        paycheck = Paycheck.objects.get(user_id=user, pay_date=date1)
        if paycheck.pay_date == date1:
            paycheck_trans = paycheck
            return paycheck_trans
    except:
        pass







