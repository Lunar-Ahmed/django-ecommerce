from django.db import models

class Pdetail(models.Model):
    pname = models.CharField(max_length=200)
    psize = models.TextField(max_length=15)
    punit = models.TextField(max_length=50)
    pdescription = models.TextField(max_length=1000)


    # pimage = models.ImageField(upload_to='images/')