from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default='sneaker1.jpg', blank=True)

    def __str__(self):
        return self.name
    

class Register(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=250)

class Login(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=250)
    
class Pdetail(models.Model):
    pname = models.CharField(max_length=200)
    pprice = models.TextField(max_length=10, null=True)
    psize = models.TextField(max_length=15)
    punit = models.TextField(max_length=50)
    pdescription = models.TextField(max_length=1000)
