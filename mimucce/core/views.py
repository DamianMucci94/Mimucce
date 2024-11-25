from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from productos.models import Product

def index(request):
    relevant_products = Product.objects.filter(is_relevant=True)
    return render(request, 'core/index.html', {'products': relevant_products})

class CustomLoginView(LoginView):
    template_name = 'core/login.html'  # Ruta a tu plantilla personalizada

    def get_success_url(self):
        return reverse_lazy('core:index')  # Redirige a la página de inicio

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('core:index')  # Redirige al inicio después de cerrar sesión
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('core:login')
        else:
            messages.error(request, 'Corrige los errores a continuación.')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})