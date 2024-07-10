from django.db import models

NULLABLE = {"null": True, "blank": True}

class Products(models.Model):
    product_name = models.CharField(max_length=225, verbose_name="продукт")
    description = models.TextField(verbose_name="описание")
    preview_img = models.ImageField(uplpad_to="product_images", verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания', auto_now=True)
    updated_at = models.DateField(verbose_name='Дата создания', auto_now=True)

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("product_name",)

class Category(models.Model):
    category_name = models.CharField(max_length=225, verbose_name="категория")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("category_name",)

