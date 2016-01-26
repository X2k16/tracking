# coding=utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from tracking.program.models import Timespan
from tracking.enquete.models import ProgramEnquete
from tracking.enquete.forms import ProgramEnqueteForm, ParticipantForm


@login_required
def index(request):

    timespans = Timespan.objects.all()
    program_enquetes = {
        e.timespan_id: e
        for e in ProgramEnquete.objects.filter(participant=request.user)
    }

    for timespan in timespans:
        # 時間帯ごとのアンケート回答を取得
        timespan.enquete = program_enquetes.get(timespan.id, None)

    context = {
        "timespans":timespans
    }
    return render(request, "enquete/index.html", context)


@login_required
def participant_form(request):
    participant = request.user

    form = ParticipantForm(instance=participant)
    if request.method == "POST":
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(settings.PROGRAM_REDIRECT_URL)

    context = {
        "form": form
    }
    return render(request, "enquete_form.html", context)



@login_required
def program_enquete(request, timespan_id):
    timespan = get_object_or_404(Timespan, id=timespan_id)
    try:
        instance = ProgramEnquete.objects.get(participant=request.user, timespan=timespan)
    except ProgramEnquete.DoesNotExist:
        instance = ProgramEnquete(participant=request.user, timespan=timespan)

    form = ProgramEnqueteForm(instance=instance)
    if request.method == "POST":
        form = ProgramEnqueteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("enquete_index")

    context = {
        "timespan":timespan,
        "form":form
    }
    return render(request, "enquete/program_enquete.html", context)
