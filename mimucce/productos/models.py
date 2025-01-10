from django.db import models

class Product(models.Model):
    CATEGORIAS = [
        ('vestido', 'Vestido'),
        ('pantalon', 'Pantalón'),
        ('calzado', 'Calzado'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='productos')
    is_relevant = models.BooleanField(default=False)
    category = models.CharField(max_length=10, choices=CATEGORIAS)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name