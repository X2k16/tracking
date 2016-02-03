# coding=utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from tracking.program.models import Timespan, ProgramAttendance
from tracking.enquete.models import ProgramEnquete
from tracking.enquete.forms import ProgramEnqueteForm, ParticipantForm, CrossEnqueteForm


@login_required
def index(request):

    program_enquetes = {
        e.timespan_id: e
        for e in ProgramEnquete.objects.filter(participant=request.user)
    }

    timespans = []
    for timespan in Timespan.objects.all():
        data = {
            "id": timespan.id,
            "name": timespan.name,
        }

        # 時間帯ごとのアンケート回答を取得
        data["enquete"] = program_enquetes.get(timespan.id, None)
        # 時間帯ごとの参加プログラム
        data["programs"] = list(ProgramAttendance.objects.filter(participant=request.user, timespan=timespan))

        timespans.append(data)

    context = {
        "timespans": timespans,
        "lottery_count": request.user.lottery_count
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
def cross_enquete(request):
    participant = request.user

    form = CrossEnqueteForm(instance=participant)
    if request.method == "POST":
        form = CrossEnqueteForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect("enquete_index")

    context = {
        "form": form
    }
    return render(request, "enquete/cross_form.html", context)


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
        "timespan": timespan,
        "form": form
    }
    return render(request, "enquete/program_enquete.html", context)
