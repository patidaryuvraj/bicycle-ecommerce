from django.urls import path
from . import views
urlpatterns = [
    path('cart',views.cart, name='cart'),
    path('add_to_cart/<int:product_id>',views.add_to_cart, name='add_to_cart'),
    path('minus_cart/<int:cart_id>',views.minus_cart,name='minus_cart'),
    path('plus_cart/<int:cart_id>',views.plus_cart,name='plus_cart'),
    path('remove/<int:cart_id>',views.remove, name='remove'),
]
