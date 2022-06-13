from django.urls import path
from .views import *
urlpatterns = [
    path("", home),
    path('dashboard/', dash),
    path('contact/', contact),
    path("aboute/", aboute),
    path("skils/", skils),
    path("login/", register)
]
