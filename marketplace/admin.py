from django.contrib import admin
from .models import Brand, Category, Item, Customer

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Customer)