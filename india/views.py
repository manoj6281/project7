from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1>50th century of ODI</h1>')


def rohith(request):
    return HttpResponse('<h1><marquee>he is the captain of india in ODI</marquee></h1>')


