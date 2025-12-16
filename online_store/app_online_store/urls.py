from django.contrib import admin
from django.urls import path
from . import views

app_name = "store"
#darkusha
#400rostik400
urlpatterns = [
    path('home/', views.home,name = 'home'),
    path('add_product/',views.add_product,name = 'add_product'),
    path('register_user/', views.register,name='register_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name = 'logout_user'),
    path('product_detail/<slug:slug>' , views.product_detail,name = 'product_detail'),
    path('profile/<str:username>',views.profile,name ='profile' ),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<slug:product_slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/decrease/<int:item_id>/', views.decrease_item, name='decrease_item'),
    path('cart/add_item/<int:item_id>/', views.add_item, name='add_item'),

]
