# encoding=utf-8

from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden


def token_login(request):
    token = request.GET.get("t")
    user = authenticate(token=token)
    if not user:
        return HttpResponseForbidden("Invalid Token")
    login(request, user)

    if not user.is_answered():
        return redirect("participant_form")
    return HttpResponseRedirect(settings.PROGRAM_REDIRECT_URL)


def unauthorized(request):
    return render(request, "unauthorized.html")
