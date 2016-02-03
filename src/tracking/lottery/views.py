# coding=utf-8
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from tracking.lottery.models import LotteryTicket


@staff_member_required
def get_lottery(request):

    if request.method == "POST" and request.POST.get("action") == "refresh":
        LotteryTicket.objects.refresh()
        return HttpResponseRedirect("")

    context = {
        "tickets": LotteryTicket.objects.all().order_by("-ordering")[:30]
    }
    return render(request, "lottery.html", context)
