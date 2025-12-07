from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from .form import FormProduct


def home(request):
    products = models.Product.objects.all()
    return render(request,"store/home.html",{"products": products})


def add_product(request):
    if request.method == 'POST':
        product = FormProduct(request.POST,request.FILES)
        if product.is_valid():
            product.save()
            redirect('store:home')
    else:
        product = FormProduct()
    return render(request,'AddProduct/add_product.html',{"product":product})