# Generated by Django 4.1.4 on 2023-06-13 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=50)),
                ('customermobile', models.CharField(max_length=15)),
                ('customersemail', models.EmailField(max_length=50)),
                ('customeraddress', models.TextField(max_length=200)),
                ('productname', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='cart')),
                ('totalprice', models.IntegerField(default=0)),
                ('productid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]