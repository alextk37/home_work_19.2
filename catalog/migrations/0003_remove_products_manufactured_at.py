# Generated by Django 5.0.6 on 2024-07-10 08:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_products_manufactured_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="manufactured_at",
        ),
    ]
