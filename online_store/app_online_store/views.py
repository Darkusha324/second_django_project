from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import models
from .form import FormProduct , RegisterUserForm


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



def register(request, ):
    if request.method == 'POST':
        form_user = RegisterUserForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('store:login_user')
    else:
        form_user = RegisterUserForm()
    return render(request, 'register/register.html', {'form_user': form_user})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("store:home")
        else:
            return render(request, "login/login.html", {"error": "Невірні дані"})
    else:
        return render(request, "login/login.html")


def logout_user(request):
    logout(request)
    return redirect("store:home")