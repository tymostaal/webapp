from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world! This is my first Django view.")
# Create your views here.
