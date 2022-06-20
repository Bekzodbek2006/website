from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import *
from .form import *
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

class Sign(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = Signup

    def get_success_url(self):
        return reverse("app:home")