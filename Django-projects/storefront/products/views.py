from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Product
from django.views import View


def newproducts(request):
    return HttpResponse('New Products')

def products(request):
    return render(request, 'products.html', {'products': Product.objects.all()})

#class ProductView(View):
def product(request, name):
    #x = {'name': str(name)}
    obj = Product.objects.get(name=name)    
    x = {'product': obj}
    return render(request, 'single-product.html', x)

def redirect(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/products/new/')