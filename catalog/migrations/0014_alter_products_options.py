# Generated by Django 5.0.6 on 2024-08-28 08:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0013_products_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="products",
            options={
                "ordering": ("product_name",),
                "permissions": [
                    (
                        "can_change_is_published",
                        "Может редактировать статус публикации",
                    ),
                    (
                        "can_change_product_description",
                        "Может редактировать количество описание",
                    ),
                    ("can_change_product_category", "Может редактировать категорию"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
