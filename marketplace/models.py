from django.conf import settings
from django.db import models

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

class Brand(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):
    items = models.ManyToManyField(Item)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
