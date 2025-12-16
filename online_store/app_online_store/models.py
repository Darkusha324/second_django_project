from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from .ua_to_en import ua_to_en


class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,blank=True)
    price =  models.DecimalField(max_digits=10,decimal_places=2)
    photograph = models.ImageField(upload_to="photograph/",blank=True,null=True,default="photograph/telephon.jpg")
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(ua_to_en(self.name))
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def total_price(self):
        return sum(item.total() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total(self):
        return self.product.price * self.quantity

