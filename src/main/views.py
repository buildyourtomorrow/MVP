from django.shortcuts import render_to_response, HttpResponseRedirect, RequestContext, HttpResponse
from django.contrib.auth.decorators import login_required
import math
import calendar
from datetime import date
import datetime


def landing_page(request):

    #<p><a class="btn btn-default" href='{% url "learnmore" %}' role="button">Learn more &raquo;</a></p>
    #<p><a class="btn btn-default" href='{% url "learnmore" %}' role="button">Learn more &raquo;</a></p>

    return render_to_response('marketing.html', locals(), context_instance=RequestContext(request))