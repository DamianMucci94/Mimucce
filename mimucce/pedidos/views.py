from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PaymentForm
from .models import Order
from productos.models import Product
from django.urls import reverse

class AddToCartView(LoginRequiredMixin, TemplateView):
    template_name = 'add_to_cart.html'  # Plantilla de confirmación de agregado al carrito
    
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        
        # Crear o actualizar la orden en estado "Pending"
        order, created = Order.objects.get_or_create(
            user=request.user,
            product=product,
            status='Pending',
            defaults={'quantity': 1, 'total_price': product.price}
        )
        if not created:
            order.quantity += 1  # Aumentar cantidad si ya existe
            order.total_price = order.quantity * product.price
            order.save()
        
        return redirect('pedidos:cart_detail')

class CartDetailView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'cart_detail.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, status='Pending')
    
class CheckoutView(LoginRequiredMixin, FormView):
    template_name = 'checkout.html'
    form_class = PaymentForm
    success_url = '/payment/success/'  # URL para cuando el pago sea exitoso

    def form_valid(self, form):
        # Aquí puedes manejar la lógica de pago, como la integración con la pasarela de pago
        try:
            # Imagina que aquí llamamos a procesar_pago() y si falla, redirige a cancelar
            # procesar_pago(form.cleaned_data)
            return super().form_valid(form)
        except Exception as e:  # Captura de errores de pago
            return redirect('pedidos:payment_cancel_page')  # Redirige a página de cancelación

class PaymentSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'payment_success.html'  # Ruta a tu plantilla de éxito

class PaymentCancelView(LoginRequiredMixin, TemplateView):
    template_name = 'payment_cancel.html'  # Ruta a tu plantilla de cancelación