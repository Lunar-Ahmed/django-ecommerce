from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pdetail

def main(request):
    mproducts = Pdetail.objects.all().values()
    template = loader.get_template('products.html')
    context = {
        'mproducts' : mproducts
    }
    return HttpResponse(template.render(context, request))

def details(request):
    pdes = Pdetail.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'pdes' : pdes
    }
    return  HttpResponse(template.render(context, request))
