from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def redirect_polls(request):
    return redirect('index', permanent=True)
