import os
from django.core.files import File
from django.shortcuts import render, get_object_or_404
from .models import Product



def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'details.html', {'product': product})


def save_product_image(image_path, product_id):
    with open(image_path, 'rb') as f:
        image_file = File(f)
        product = Product.objects.get(pk=product_id)
        product.image.save(os.path.basename(image_path), image_file, save=True)

# from django.http import HttpResponse
# from django.template import loader
# from .models import Pdetail

# def main(request):
#     mproducts = Pdetail.objects.all().values()
#     template = loader.get_template('products.html')
#     context = {
#         'mproducts' : mproducts
#     }
#     return HttpResponse(template.render(context, request))

# def details(request):
#     pdes = Pdetail.objects.get(id=id)
#     template = loader.get_template('details.html')
#     context = {
#         'pdes' : pdes
#     }
#     return  HttpResponse(template.render(context, request))
