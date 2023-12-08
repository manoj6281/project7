from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def williamson(request):
    return HttpResponse('<h1><marquee>he is score is 50 plus in today</h1<marquee>')


def ravindra(request):
    return HttpResponse('<h1><marquee>he is wonderful youngstar batsman</h1<marquee>')