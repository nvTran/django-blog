from django.http import HttpResponse
from django.shortcuts import render



def about(request):
    return render(request, "about.html")


def donate(request):
    return render(request, "donate.html")

