#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello, I'm here")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("Hello, I'm here and about")
    return render(request, 'about.html')