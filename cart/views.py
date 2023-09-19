from django.shortcuts import render,redirect
from product.models import Product
from .models import Cart
from website.models import Customer
# from django.http import JsonResponse
# Create your views here.
def add_to_cart(request, product_id):
    username = request.session['username']
    customer = Customer.objects.filter(username=username)
    for c in customer:
        customername = c.name
        customersemail = c.email
        customermobile = c.mobile
        customeraddress = c.address
    productid = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        productname = p.product_name
        price = p.price 
        image = p.image
        
        
    totalprice = price
    try:
        cart = Cart.objects.get(customername= customername, productname=productname)
        return redirect('cart')
    except:
        cart=Cart(customername=customername,customermobile=customermobile,customersemail=customersemail,customeraddress=customeraddress,productname=productname, price=price,image=image,productid=productid,totalprice=totalprice)
        cart.save()
        return redirect('productview')


def cart(request):
    if request.session.has_key('username'):
        username = request.session['username']
        customer = Customer.objects.filter(username=username)
        for c in customer:
            name = c.name
        totalitem = Cart.objects.filter(customername=name).count()
        cart = Cart.objects.filter(customername=name)
        return render(request,'cart.html',{'cart':cart,'name':name,'totalitem':totalitem})
    else:
        totalitem = Cart.objects.all().count()
        cart = Cart.objects.all()
        return render(request,'cart.html',{'cart':cart,'totalitem':totalitem})

def plus_cart(request,cart_id):
    c = Cart.objects.get(id = cart_id)
    c.quantity+=1
    c.totalprice = c.quantity*c.price
    c.save()
    return redirect('cart')
def minus_cart(request,cart_id):
    c = Cart.objects.get(id = cart_id)
    c.quantity-=1    
    if c.quantity>=1:
        c.totalprice = c.totalprice-c.price
        c.save()
    else:
        c.quantity=0
    return redirect('cart')
def remove(request,cart_id):
    c = Cart.objects.get(id = cart_id)
    c.delete()
    return redirect('cart')