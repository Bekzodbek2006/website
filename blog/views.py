from django.shortcuts import render, redirect
from .models import *
from .form import Registiration
def home(request):
    return render(request, 'home.html')

def dash(request):
    fun = Chart.objects.all()
    return render(request, 'charts.html', {"base": fun})

def contact(request):
    return render(request, 'contactus.html')

def aboute(request):
    return render(request, 'aboute.html')

def skils(request):
    return render(request, "skils.html")

def register(request):
    if request.method == "POST":
        form = Registiration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = Registiration()
    return render(request, "form.html", {'form': form})