from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', views.CartDetailView.as_view(), name='cart_detail'),
    path('checkout/confirm/', views.CheckoutView.as_view(), name='checkout_page'),
    path('payment/success/', views.PaymentSuccessView.as_view(), name='payment_success_page'),
    path('payment/cancel/', views.PaymentCancelView.as_view(), name='payment_cancel_page'),
]