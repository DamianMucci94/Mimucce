from django.db import models
from productos.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),  # Primer valor se guarda en la base de datos, el segundo se muestra
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Agregar choices

    def __str__(self):
        return f"{self.product.name} - {self.status}"
    
    def mark_as_paid(self):
        """Marca la orden como 'Paid'."""
        self.status = 'paid'
        self.save()

    def mark_as_cancelled(self):
        """Marca la orden como 'Cancelled'."""
        self.status = 'cancelled'
        self.save()