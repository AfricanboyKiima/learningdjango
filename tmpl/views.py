from django.shortcuts import render
from django.views import views

def simple(request):
    return render(request,'tmpl/simple.html')