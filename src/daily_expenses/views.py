from django.shortcuts import render_to_response, HttpResponseRedirect, RequestContext, HttpResponse
from django.contrib.auth.decorators import login_required
from income.models import Income, Paycheck
from monthly_bills.models import Bill, BillTotal
from monthly_bills.functions import *
from django.contrib import messages
from .functions import *
from .forms import CashForm, DailyExpenseForm, DatePickerForm, EditExpenseForm


now = date.today()
#now1 = now1.replace(day=20)

@login_required()
def dashboard(request):
    now = date.today()
    user = request.user.id
    x = 0
    y = 0
    z = 0
    try:
        x = Income.objects.get(user_id=user)
        y = BillTotal.objects.get(user_id=user)
        z = Paycheck.objects.filter(user_id=user).order_by('pay_date')[0]
    except:
        pass

    if x == False:
        messages.success(request, 'We need your income before calculating your dialy budget')
        return HttpResponseRedirect('/income/')

    elif y == False:
        messages.success(request, 'Not so fast, we need to know what bills you pay monthly.')
        return HttpResponseRedirect('/bills/')

    else:
        first_paycheck = z.pay_date

        if first_paycheck > now:
            messages.success(request, "No daily budget is available since you have not yet gotten paid.")
            return render_to_response('daily_budget/dashboard1.html', locals(), context_instance=RequestContext(request))

        else:
            beginning_daily_budget_function(user, now)
            beginning_period_budget_function(user, now)
            daily_expense_sum_to_transaction(user, now)
            ending_daily_budget_function(user, now)
            ending_period_budget_function(user, now)

            update_daily_period_budget_function(user, now)

            transactions = create_transaction_function(user, now)
            daily_budget = daily_budget_function(user, now)
            beginning_daily_budget = get_beginning_daily_budget(user, now)
            beginning_period_budget = get_beginning_period_budget(user, now)
            daily_expenses = DailyExpense.objects.filter(user_id=user, date=now)
            next_paycheck = get_very_next_paycheck(user, now)
            get_paychecks_to_show = get_all_paychecks_to_show(user, now)

            return render_to_response('daily_budget/dashboard.html', locals(), context_instance=RequestContext(request))


@login_required()
def expense(request):
    user = request.user.id

    if request.method == "POST":
        form = DailyExpenseForm(request.POST)
        if form.is_valid():

            exp_date = form.cleaned_data['date']
            exp_date1 = form.cleaned_data['date']

            instance = form.save(commit=False)
            instance.user_id = user
            instance.amount = form.cleaned_data['amount'] * -1
            instance.save()
            instance.to_transaction_sum = daily_expense_sum_to_transaction(user, exp_date)
            instance.save()

            if exp_date < now:

                first_check = Paycheck.objects.filter(user_id=user).order_by('id')[0]
                if exp_date < first_check.pay_date:
                    messages.success(request, 'hmmm, the date you entered is a little funky.  '
                                              'Are you sure you got a paycheck on or after that date?')
                    return HttpResponseRedirect('/daily_budget/datepicker')

                else:
                    create_transaction_function(user, exp_date)
                    ending_daily_budget_function(user, exp_date)
                    ending_period_budget_function(user, exp_date)

                    return HttpResponseRedirect('/daily_budget/')

            elif exp_date == now:

                create_transaction_function(user, now)
                ending_daily_budget_function(user, now)
                ending_period_budget_function(user, now)

                return HttpResponseRedirect('/daily_budget/')

            else:
                pass

                return HttpResponseRedirect('/daily_budget/')

        return render_to_response('daily_budget/expense.html', locals(), context_instance=RequestContext(request))

    form = DailyExpenseForm

    return render_to_response('daily_budget/expense.html', locals(), context_instance=RequestContext(request))


@login_required()
def cash(request):

    form = CashForm

    return render_to_response('daily_budget/cash.html', locals(), context_instance=RequestContext(request))


@login_required()
def calculations(request):

    return render_to_response('daily_budget/calculations.html', locals(), context_instance=RequestContext(request))


@login_required()
def datepicker(request):

    user = request.user.id

    if request.method == 'POST':
        form = DatePickerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = user
            instance.save()
            now = form.cleaned_data['date']
            first_check = Paycheck.objects.filter(user_id=user).order_by('id')[0]
            if now < first_check.pay_date:
                messages.success(request, 'hmmm, the date you entered is a little funky.  Are you sure you got a paycheck on or after that date?')
                return HttpResponseRedirect('/daily_budget/datepicker')
            else:
                beginning_daily_budget_function(user, now)
                beginning_period_budget_function(user, now)
                daily_expense_sum_to_transaction(user, now)
                ending_daily_budget_function(user, now)
                ending_period_budget_function(user, now)

                update_daily_period_budget_function(user, now)

                transactions = create_transaction_function(user, now)
                daily_budget = daily_budget_function(user, now)
                beginning_daily_budget = get_beginning_daily_budget(user, now)
                beginning_period_budget = get_beginning_period_budget(user, now)
                daily_expenses = DailyExpense.objects.filter(user_id=user, date=now)
                next_paycheck = get_very_next_paycheck(user, now)
                get_paychecks_to_show = get_all_paychecks_to_show(user, now)

                return render_to_response('daily_budget/dashboard.html', locals(), context_instance=RequestContext(request))

        return render_to_response('daily_budget/date.html', locals(), context_instance=RequestContext(request))

    form = DatePickerForm()

    return render_to_response('daily_budget/date.html', locals(), context_instance=RequestContext(request))


@login_required()
def delete(request, id):

    object1 = DailyExpense.objects.get(id=id)
    DailyExpense.objects.get(id=id).delete()
    date1 = object1.date
    user = request.user.id
    daily_expense_sum_to_transaction(user, date1)

    return HttpResponseRedirect('/daily_budget/')


@login_required()
def edit_expense(request, id):

    user = request.user.id
    d = DailyExpense.objects.get(id=id)

    if request.method == "POST":
        form = EditExpenseForm(request.POST)
        if form.is_valid():
            d.user_id = user
            d.description = form.cleaned_data['description']
            d.amount = (abs(form.cleaned_data['amount'])) * -1
            d.date = form.cleaned_data['date']
            d.save()

            object1 = DailyExpense.objects.get(id=id)
            exp_date = object1.date
            object1.to_transaction_sum = daily_expense_sum_to_transaction(user, exp_date)
            object1.save()

            return HttpResponseRedirect('/daily_budget/')

    form = EditExpenseForm(instance=d)

    return render_to_response('daily_budget/edit.html', locals(), context_instance=RequestContext(request))


