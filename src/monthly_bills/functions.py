from income.models import Paycheck, Income
from monthly_bills.models import *
from .models import *
import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from daily_expenses.functions import *


#Generates year long daily beginning, ending and period beginning and ending balances.
def daily_period_generator(user):
    try:
        first_paycheck = Paycheck.objects.filter(user_id=user).order_by('pay_date')[0]
        d = first_paycheck.pay_date
        y = timedelta(days=0)
        for day in range(5):
            d = d + y
            beginning_daily_budget_function(user, d)
            ending_daily_budget_function(user, d)
            beginning_period_budget_function(user, d)
            ending_period_budget_function(user, d)
            y = timedelta(days=1)
    except:
        pass



