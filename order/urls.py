from django.urls import path
from . import views
urlpatterns = [

    path('checkout_session/<int:cart_id>',views.checkout_session,name='checkout_session'),
    path('pay_success',views.pay_success,name='pay_success'),
    path('pay_cancel',views.pay_cancel,name='pay_cancel'),
    path('orderdetail',views.orderdetail, name='orderdetail'),
    path('bill/<int:Orderid>',views.bill,name='bill'),
    path('cancle/<int:Order_id>',views.cancle,name='cancle')

]