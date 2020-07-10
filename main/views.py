from django.conf import settings
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from main.models import Command


@cache_page(settings.STATIC_PAGE_CACHE_SECONDS)
def index(request):
    hostnames = ["Disorder", "workstation", "randomhostname"]

    return render(request, "layout.html", {
        "commands": Command.objects.all(),
        "hostnames": hostnames
    })
