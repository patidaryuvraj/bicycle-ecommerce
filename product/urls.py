from django.urls import path
from . import views
urlpatterns = [
        path('productview',views.productview, name='productview'),
        path('productdetails/<int:product_id>',views.productdetails, name='productdetails'),
        path('search',views.search, name='search'),
]
