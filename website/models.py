from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    mobile = models.CharField(max_length=15)
    comment = models.CharField(max_length=1000)

    class Meta:
        db_table = "contact"
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75, unique=True)
    mobile = models.CharField(max_length=15,unique=True)
    role = models.CharField(max_length=10,default='Customer')
    address = models.TextField(max_length=200)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "customer"