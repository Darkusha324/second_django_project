from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .form import FormProduct , RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    return render(request,"store/home.html",{"products": products,"categories":categories})

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

def add_to_cart(request, product_slug):
    product = get_object_or_404(models.Product, slug=product_slug)
    cart = request.user.cart

    item, created = models.CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1

    item.save()
    return redirect('store:home')


def add_item(request,item_id):
    item = get_object_or_404(models.CartItem, id=item_id, cart=request.user.cart)

    item.quantity +=1
    item.save()
    return redirect('store:cart',username=request.user.username)


def decrease_item(request, item_id):
    item = get_object_or_404(models.CartItem, id=item_id, cart=request.user.cart)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('store:cart', username=request.user.username)

def cart_view(request,username):
    cart = request.user.cart
    items = cart.items.all()
    total = cart.total_price()

    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })


def product_category(request,slug):
        category = get_object_or_404(models.Category, slug=slug)
        products = category.products.all()
        categories = models.Category.objects.all()

        data = {
            'products': products,
            'categories': categories,
            'selected_category': category
        }

        return render(request, 'store/home.html',data)