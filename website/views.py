from django.shortcuts import render,redirect
from cart.models import Cart
from .models import Contact, Customer
# Create your views here.
def index(request):
    totalitem = Cart.objects.all().count()
    return render(request,'index.html',{'totalitem':totalitem})
def home(request):
    totalitem = Cart.objects.all().count()
    return render(request,'home.html',{'totalitem':totalitem})
def about(request):
    totalitem = Cart.objects.all().count()
    return render(request,'aboutus.html',{'totalitem':totalitem})
def signup(request):
    totalitem = Cart.objects.all().count()
    return render(request,'signup.html',{'totalitem':totalitem})
def signin(request):
    totalitem = Cart.objects.all().count()
    return render(request,'signin.html',{'totalitem':totalitem})
def contact(request):
    totalitem = Cart.objects.all().count()
    return render(request,'contactus.html',{'totalitem':totalitem})
def contactuspage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        comment = request.POST['comment']

        contact = Contact(name = name, email = email, mobile = mobile, comment = comment)
        contact.save()
        return redirect('contact')
    else:
        return redirect('home')

def signuppage(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        username = request.POST['username']
        paswd = request.POST['password']

        try:
            customer=Customer.objects.get(email=email,mobile=mobile,username=username)
            return render(request,'signup.html',{'error':"Customer Already Exists...!!!"})
            
        except:
            customer = Customer(name = name,email = email,mobile=mobile,address=address ,username = username, password = paswd)
            customer.save()
            return render(request,'signin.html',{'msg':"Registered Successfully...!!!"})
    else:
        return render(request,'signup.html',{'error':"Invalid User Request...!!!"})

def signinpage(request):
    if request.method=="POST":
        username = request.POST['username']
        paswd = request.POST['password']

        
        customer=Customer.objects.filter(username=username,password=paswd)
        if customer:
            
            request.session['username'] = username
            # request.session['role'] = 'Customer'
            
            return redirect('productview')
        else:    
            return render(request,'signin.html',{'error':"Invalid Detail...!!!"})
    else:
        return render(request,'signin.html',{'error':"Invalid User Request...!!!"})

def logout(request):

    if request.session.has_key('username'):
        del request.session['username']
        totalitem = Cart.objects.all().count()
        return render(request,'index.html',{'totalitem':totalitem})
    else:
        # totalitem = Cart.objects.all().count()
        return redirect('home')
        # return render(request,'home.html')
