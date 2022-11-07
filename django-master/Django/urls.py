from django.http import HttpResponse

def index(request):
    from django.shortcuts import render

def about(request):
    return HttpResponse("Hellow ABout")


def article(request, year):
    return HttpResponse(f"{year}")