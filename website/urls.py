from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),

    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('contactuspage',views.contactuspage, name='contactuspage'),
    path('signuppage',views.signuppage, name='signuppage'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('logout',views.logout,name='logout'),
]