from django.shortcuts import render
# from .forms import RegistrationForm
from .models import Item


def index(req):
    items = Item.objects.all()
    return render(req, 'marketplace/index.html', {'title': 'Магазин', 'items': items})


def item(req):
    return render(req, f'marketplace/item/{item.id}')


def cart(req):
    return render(req, 'marketplace/cart.html')


# def login(req):
#     return render(req, 'marketplace/login.html')


# def registration(req):
#     form = RegistrationForm()
#     context = {
#         'form': form
#     }
#     return render(req, 'marketplace/registration.html', context)