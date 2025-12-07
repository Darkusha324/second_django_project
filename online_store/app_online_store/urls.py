from django.contrib import admin
from django.urls import path
from . import views

app_name = "store"
#darkusha
#400rostik400
urlpatterns = [
    path('home/', views.home,name = 'home'),
    path('add_product/',views.add_product,name = 'add_product')
]
