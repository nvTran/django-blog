from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Welcome to the homepage")
    return render(request, "homepage.html")

def about(request):
    # return HttpResponse("This is the about page")
    return render(request, "about.html")

