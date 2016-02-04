# encoding=utf-8

from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from tracking.heatmap import generate_heatmap

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


def heatmap_png(request):
    response = HttpResponse(content_type="image/png")
    return generate_heatmap(response)
