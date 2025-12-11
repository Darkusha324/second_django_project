from django.db import models
from django.utils.text import slugify

def ua_to_en(text):
    mapping = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g',
        'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
        'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ю': 'yu', 'я': 'ya', 'ь': '', '’': '', "'": ''
    }

    result = ""
    for char in text.lower():
        result += mapping.get(char, char)
    return result


class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,blank=True)
    price =  models.DecimalField(max_digits=10,decimal_places=2)
    photograph = models.ImageField(upload_to="photograph/",blank=True,null=True,default="photograph/telephon.jpg")
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

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