# encoding=utf-8

from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from tracking.forms import ParticipantForm


def token_login(request):
    token = request.GET.get("t")
    user = authenticate(token=token)
    if not user:
        return HttpResponseForbidden("Invalid Token")
    login(request, user)

    if not user.is_answered():
        return redirect("enquete")
    return redirect("index")


@login_required
def participant_form(request):
    participant = request.user

    form = ParticipantForm(instance=participant)
    if request.method == "POST":
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form
    }
    return render(request, "enquete_form.html", context)


@login_required
def index(request):
    return render(request, "index.html")


def unauthorized(request):
    return HttpResponse("Unauthorized", status=401)
