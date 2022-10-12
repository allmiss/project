from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('cart', views.cart, name='cart'),
    # path('registration', views.registration, name='registration'),
    # path('login', views.login, name='login'),

]
