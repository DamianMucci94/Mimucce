# Generated by Django 5.1.1 on 2025-01-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='productos'),
        ),
    ]
