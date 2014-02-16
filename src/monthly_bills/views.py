from django.shortcuts import render_to_response, HttpResponseRedirect, RequestContext
from .forms import BillForm
from .models import Bill, BillTotal
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date
from .functions import *


@login_required()
def dashboard(request):

    user = request.user.id

    bills_query = Bill.objects.filter(user=user).values()

    var = 0
    for bill in bills_query:
        var = var + bill['amount']

    return render_to_response('monthly_bills/dashboard.html', locals(), context_instance=RequestContext(request))


@login_required()
def add(request):

    user = request.user.id
    now = date.today()

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            bills_query = Bill.objects.filter(user_id=user).values()

            var = 0
            for bill in bills_query:
                var = var + bill['amount']

            weekly = (var * 12) / 52
            daily = weekly / 7
            BillTotal.objects.filter(user_id=user).delete()
            BillTotal.objects.create(user_id=user,
                                     monthly_total=var,
                                     weekly=weekly,
                                     daily=daily)
            daily_period_generator(user)

            return HttpResponseRedirect('/bills/')

        return render_to_response('monthly_bills/add.html', locals(), context_instance=RequestContext(request))

    form = BillForm

    return render_to_response('monthly_bills/add.html', locals(), context_instance=RequestContext(request))


@login_required()
def edit(request, u):

    user = request.user.id

    d = Bill.objects.get(id=u)

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():

            d.description = form.cleaned_data['description']
            d.amount = form.cleaned_data['amount']
            d.save()

            bills_query = Bill.objects.filter(user_id=user).values()

            var = 0
            for bill in bills_query:
                var = var + bill['amount']

            weekly = (var * 12) / 52
            daily = weekly / 7
            BillTotal.objects.filter(user_id=user).delete()
            BillTotal.objects.create(user_id=user,
                                     monthly_total=var,
                                     weekly=weekly,
                                     daily=daily)
            daily_period_generator(user)

            return HttpResponseRedirect('/bills/')

        return render_to_response('monthly_bills/edit.html', locals(), context_instance=RequestContext(request))

    form = BillForm(instance=d)

    return render_to_response('monthly_bills/edit.html', locals(), context_instance=RequestContext(request))


@login_required()
def delete(request, u):

    user = request.user.id

    Bill.objects.get(id=u).delete()
    BillTotal.objects.filter(user_id=user).delete()

    bills_query = Bill.objects.filter(user_id=user).values()

    var = 0
    for bill in bills_query:
        var = var + bill['amount']

        weekly = (var * 12) / 52
        daily = weekly / 7
        BillTotal.objects.filter(user_id=user).delete()
        BillTotal.objects.create(user_id=user,
                                 monthly_total=var,
                                 weekly=weekly,
                                 daily=daily)
    daily_period_generator(user)

    return HttpResponseRedirect('/bills/')





