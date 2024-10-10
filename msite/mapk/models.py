from django.db import models

class Pdetail(models.Model):
    pname = models.CharField(max_length=200)
    pprice = models.TextField(max_length=10, null=True)
    psize = models.TextField(max_length=15)
    punit = models.TextField(max_length=50)
    pdescription = models.TextField(max_length=1000)
