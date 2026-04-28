from django.contrib import admin
from .models import*


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}   # автоматичне створення slug
    search_fields = ('name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'user', 'category', 'creation_date')
    list_filter = ('category', 'user', 'creation_date')
    search_fields = ('name', 'description')
    readonly_fields = ('creation_date',)
    prepopulated_fields = {"slug": ("name",)}   # slug генерується з name



class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price')
    inlines = [CartItemInline]



class OrderCartItemInline(admin.TabularInline):
    model = OrderCartItem
    extra = 1


@admin.register(OrderCart)
class OrderCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price')
    inlines = [OrderCartItemInline]



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'city', 'postal_code', 'create_at', 'email')
    list_filter = ('city', 'create_at')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    readonly_fields = ('create_at',)
