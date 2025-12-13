from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import models
from .form import FormProduct , RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    products = models.Product.objects.all()
    return render(request,"store/home.html",{"products": products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = FormProduct(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('store:profile',username = request.user.username)
    else:
        form = FormProduct()
    return render(request,'AddProduct/add_product.html',{"product":form})



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


def product_detail (request, slug ):
    product = models.Product.objects.get(slug=slug)
    return render(request,'product_detail/product_detail.html',{"product":product})


@login_required
def profile(request,username):
    user = User.objects.get(username=username)
    products = models.Product.objects.filter(user_id=request.user)
    return render(request,'profile/profile.html',{'user':user,'products':products})