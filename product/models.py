from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=500)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=10000)
    image= models.ImageField(upload_to="product",default="")

    class Meta:
        db_table= "product"