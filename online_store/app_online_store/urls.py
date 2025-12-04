from django.contrib import admin
from django.urls import path
from . import views

app_name = "store"
#darkusha
#400rostik400
urlpatterns = [
    path('home/', views.home,name = 'home'),
]
