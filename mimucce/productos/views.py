from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from .models import Product

class ListaProductosView(ListView):
    model = Product
    template_name = 'productos/listaproducto.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Obtener el queryset base
        queryset = super().get_queryset()
        # Filtrar por categoría si está presente en los kwargs
        categoria = self.kwargs.get('categoria')
        if categoria:
            queryset = queryset.filter(category=categoria)
        # Filtrar por el término de búsqueda si está presente en la consulta GET
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset
        #categoria = self.kwargs.get('categoria')
        #if categoria:
        #    return Product.objects.filter(category=categoria)
        #return Product.objects.all()
    
class ProductoDetalleView(DetailView):
    model = Product
    template_name = 'productos/producto.html'
    context_object_name = 'product'
