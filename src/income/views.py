from django.shortcuts import render_to_response, HttpResponseRedirect, RequestContext, HttpResponse
from .forms import PaycheckEditForm, IncomeForm, IncomeEditForm
from django.contrib.auth.decorators import login_required
from monthly_bills.functions import *
from .functions import *
from .models import *
from datetime import date
import datetime

now = date.today()

@login_required()
def dashboard(request):
    month = now.month
    user = request.user.id
    paychecks = get_paychecks_function(user)
    income = get_income_funtion(user)
    frequency2 = get_frequency_function(user)
    till_next_paycheck_function(user, now)

    return render_to_response('income/dashboard.html', locals(), context_instance=RequestContext(request))


@login_required()
def paycheck_edit(request, u):

    user = request.user.id

    d = Paycheck.objects.get(id=u)

    if request.method == 'POST':
        form = PaycheckEditForm(request.POST)
        if form.is_valid():
            d.description = form.cleaned_data['description']
            d.amount = form.cleaned_data['amount']
            d.pay_date = form.cleaned_data['pay_date']
            d.save()
            daily_period_generator(user)

            return HttpResponseRedirect('/income/')

        return render_to_response('income/edit.html', locals(), context_instance=RequestContext(request))

    form = PaycheckEditForm(instance=d)

    return render_to_response('income/edit.html', locals(), context_instance=RequestContext(request))


@login_required()
def delete(request, u):
    user = request.user.id
    try:
        Paycheck.objects.get(id=u).delete()
    except:
        pass

    daily_period_generator(user)

    return HttpResponseRedirect('/income/')


def income_edit(request, u):

    user = request.user.id
    d = Income.objects.get(id=u)

    if request.method == 'POST':
        form = IncomeEditForm(request.POST)
        if form.is_valid():
            object = Income.objects.get(user_id=user)
            object.description = form.cleaned_data['description']
            object.amount = form.cleaned_data['amount']
            object.frequency = form.cleaned_data['frequency']
            object.pay_date = form.cleaned_data['start_date']
            object.save()

            if object.frequency == "52":
                weekly_paycheck_create_function(user, now, object.pay_date)
                daily_period_generator(user)

                return HttpResponseRedirect('/income/')

            elif object.frequency == "26":
                biweekly_paycheck_create_function(user, now, object.pay_date)
                daily_period_generator(user)

                return HttpResponseRedirect('/income/')

            elif object.frequency == "24":
                if now.day < 15:
                    bimonthly_paycheck_create_function1(user, now, object.pay_date)
                    daily_period_generator(user)

                    return HttpResponseRedirect('/income/')
                else:
                    bimonthly_paycheck_create_function(user, now, object.pay_date)
                    daily_period_generator(user)

                    return HttpResponseRedirect('/income/')

            elif object.frequency == "12":
                monthly_paycheck_create_function(user, now, object.pay_date)
                daily_period_generator(user)

                return HttpResponseRedirect('/income/')

        return render_to_response('income/edit_income.html', locals(), context_instance=RequestContext(request))

    form = IncomeEditForm(instance=d)

    return render_to_response('income/edit_income.html', locals(), context_instance=RequestContext(request))


@login_required()
def add(request):

    user = request.user.id

    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = user
            instance.save()

            frequency1 = form.cleaned_data['frequency']
            next_paycheck = form.cleaned_data['next_paycheck']

            if frequency1 == '52':
                weekly_paycheck_create_function(user, now, next_paycheck)
                daily_period_generator(user)

                return HttpResponseRedirect('/income/')

            elif frequency1 == '26':
                biweekly_paycheck_create_function(user, now, next_paycheck)
                daily_period_generator(user)

                return HttpResponseRedirect('/income/')

            elif frequency1 == "24":
                if now.day < 15:
                    bimonthly_paycheck_create_function1(user, now, next_paycheck)
                    daily_period_generator(user)

                    return HttpResponseRedirect('/income/')
                else:
                    bimonthly_paycheck_create_function(user, now, next_paycheck)
                    daily_period_generator(user)

                    return HttpResponseRedirect('/income/')

            elif frequency1 == "12":
                monthly_paycheck_create_function(user, now, next_paycheck)
                daily_period_generator(user)

                return HttpResponseRedirect('/income/')

        return render_to_response('income/add.html', locals(), context_instance=RequestContext(request))

    form = IncomeForm

    return render_to_response('income/add.html', locals(), context_instance=RequestContext(request))

@login_required()
def delete_income(request):
    user = request.user.id
    Income.objects.get(user_id=user).delete()
    Paycheck.objects.filter(user_id=user).delete()
    till_next_paycheck_function(user, now)
    daily_period_generator(user)
    return HttpResponseRedirect('/income/')


@login_required()
def frequency(request):
    user = request.user.id
    now = date.today()
    income = Income.objects.get(user_id=user)

    if income.frequency == "52":
        if income.start_date < now:
            gap = abs(income.start_date - now)
            passed_checks = int(gap.days / 7) + 1

            days_in_week = datetime.timedelta(days=0)
            for period in range(passed_checks):
                next_paycheck = income.start_date + days_in_week
                Paycheck.objects.create(user_id=user,
                                        description=income.description,
                                        amount=income.amount,
                                        pay_date=next_paycheck,
                                        active="True")
                income.start_date = next_paycheck
                days_in_week = datetime.timedelta(days=7)

            daily_period_generator(user)
            return HttpResponseRedirect('/income/')

        if income.start_date == now:
            Paycheck.objects.create(user_id=user,
                                    description=income.description,
                                    amount=income.amount,
                                    pay_date=income.start_date,
                                    active="True")

            daily_period_generator(user)
            return HttpResponseRedirect('/income/')

        if income.start_date > now:
            pass

            return HttpResponseRedirect('/income/')

    return HttpResponseRedirect('//')


@login_required()
def dashboard11(request):

    return HttpResponseRedirect('/income/')


@login_required()
def dashboard12(request):

    return HttpResponseRedirect('/income/')




















