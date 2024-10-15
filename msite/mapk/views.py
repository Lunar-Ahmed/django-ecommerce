import os
from django.core.files import File
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .forms import Login


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



def reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            return redirect('login')  # Redirect after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'regform.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')  # Redirect to a success page
            else:   
                form.add_error(None, 'Invalid email or password')
    else:
        form = Login()
    return render(request, 'regform.html', {'form': form})


# ----------------------------------------
#             user.set_password(form.cleaned_data['password'])
#             user.save()



# def reg(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('success')
#         else:
#             form = RegistrationForm()
#         return render(request, 'regform.html', {'form': form})

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
