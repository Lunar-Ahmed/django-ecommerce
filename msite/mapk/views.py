from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pdetail

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def details(request):
    pdes = Pdetail.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'pdes' : pdes
    }
    return  HttpResponse(template.render())
