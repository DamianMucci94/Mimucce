from django.shortcuts import render

from productos.models import Product

def index(request):
    relevant_products = Product.objects.filter(is_relevant=True)
    return render(request, 'core/index.html', {'products': relevant_products})