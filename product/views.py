from django.shortcuts import render,redirect
from . models import Product
from cart.models import Cart
from website.models import Customer
# Create your views here.
def productview(request):
    if request.session.has_key('username'):
        username = request.session['username']
        customer = Customer.objects.filter(username=username)
        for c in customer:
            name = c.name
        prod = Product.objects.all()
        totalitem = Cart.objects.filter(customername = name).count()
        return render(request,'productview.html',{'prod':prod,'name':name,'totalitem':totalitem})
    else:
        totalitem = Cart.objects.all().count()
        return render(request,'home.html',{'totalitem':totalitem})
def productdetails(request,product_id):
    # totalitem = Cart.objects.all().count()
    prods = Product.objects.get(id=product_id)

    return render(request,'productdetails.html',{'prods':prods})
def search(request):
    if request.session.has_key('username'):
        username = request.session['username']
        query = request.GET.get('query')
        search = Product.objects.filter(product_name__contains=query)
        customer = Customer.objects.filter(username=username)
        for c in customer:
            name = c.name

        totalitem = Cart.objects.filter(customername = name).count()
        return render(request,'search.html',{'search':search,'name':name,'query':query,'totalitem':totalitem})
    else:
        totalitem = Cart.objects.all().count()
        return render(request,'home.html',{'totalitem':totalitem})