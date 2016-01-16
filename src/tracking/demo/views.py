# coding=utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tracking.demo.forms import TouchForm


@login_required
def index(request):

    touch_form = TouchForm()
    if request.method == "POST" and request.POST.get("_action") == "touch":
        touch_form = TouchForm(request.POST)
        if touch_form.is_valid():
            touch_form.save()
            return HttpResponseRedirect()

    context = {
        "touch_form": touch_form
    }
    return render(request, "demo/index.html", context)
