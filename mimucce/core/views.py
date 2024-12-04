from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from productos.models import Product
from .forms import CustomUserCreationForm  # Importa tu formulario personalizado


def index(request):
    relevant_products = Product.objects.filter(is_relevant=True)
    return render(request, 'core/index.html', {'products': relevant_products})

class CustomLoginView(LoginView):
    template_name = 'core/login.html'  # Ruta a tu plantilla personalizada

    def get_success_url(self):
        return reverse_lazy('core:index')  # Redirige a la página de inicio

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('core:index')  # Redirige al inicio después de cerrar sesión
    
class RegisterView(FormView):
    template_name = 'core/register.html'  # Ruta a tu plantilla personalizada
    form_class = CustomUserCreationForm    # Formulario que se utilizará
    success_url = reverse_lazy('core:login')  # Redirige al login después del registro

    def form_valid(self, form):
        form.save()  # Guarda al nuevo usuario
        messages.success(self.request, 'Tu cuenta ha sido creada exitosamente. Ahora puedes iniciar sesión.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Corrige los errores a continuación.')
        return super().form_invalid(form)