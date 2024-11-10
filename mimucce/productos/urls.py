from django.urls import path
from .views import ListaProductosView, ProductoDetalleView

app_name = 'productos'

urlpatterns = [
    path('list', ListaProductosView.as_view(), name='lista_productos'),
    path('list/<str:categoria>/', ListaProductosView.as_view(), name='lista_productos_categoria'),
    path('producto/<int:pk>/', ProductoDetalleView.as_view(), name='detalle_producto'),
]