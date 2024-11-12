from django.shortcuts import render
from django.contrib.auth.views import LoginView
from productos.models import Product

def index(request):
    relevant_products = Product.objects.filter(is_relevant=True)
    return render(request, 'core/index.html', {'products': relevant_products})

class CustomLoginView(LoginView):
    template_name = 'core/login.html'  # Ruta a tu plantilla personalizada