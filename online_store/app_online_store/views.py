from django.http import HttpResponse
from django.shortcuts import render
from . import models
def home(request):
    products = models.Product.objects.all()
    return render(request,"store/home.html",{"products": products})
