from django.shortcuts import render

from main.models import Command


def index(request):
    return render(request, "layout.html", {
        "commands": Command.objects.all()
    })
