from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('home')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Shoos(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_shoos')
    name = models.CharField('Shoose name', max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shoos'
        verbose_name_plural = 'Shooses'

class Firm(models.Model):
    shoose = models.ForeignKey(Shoos, on_delete=models.CASCADE, related_name='shoosefirm')
    name = models.CharField('Firm name', max_length=50)
    about = models.TextField('Firm about')
    img = models.ImageField('Firm image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Firm'
        verbose_name_plural = 'Firms'

class Cart(models.Model):
    name = models.CharField('Cart name', max_length=100)
    numbers = models.IntegerField('Cart numbers')
    user = models.CharField('User name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'