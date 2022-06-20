from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path("", home, name="home"),
    path('dashboard/', dash),
    path('contact/', contact),
    path("aboute/", aboute),
    path("skils/", skils),
    path("login/", register),
    path("signup/", Sign.as_view(), name="signup")
]
