from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count

NULLABLE = {"null": True, "blank": True}

class Products(models.Model):
    product_name = models.CharField(max_length=225, verbose_name="продукт")
    description = models.TextField(verbose_name="описание")
    preview_img = models.ImageField(upload_to="product_images", verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="категория")
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания', auto_now=True, **NULLABLE)
    updated_at = models.DateField(verbose_name='Дата изменения', auto_now=True, **NULLABLE)
    # manufactured_at = models.DateField(verbose_name='Дата производства', **NULLABLE)

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("product_name",)

class Category(models.Model):
    category_name = models.CharField(max_length=225, verbose_name="категория")
    description = models.TextField(verbose_name="описание")
    has_products = models.BooleanField(verbose_name="Есть продукты", default=False)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("category_name",)

@receiver(post_save, sender=Products)
def update_category_has_products(sender, instance, **kwargs):
    category = instance.category
    category.has_products = Products.objects.filter(category=category).exists()
    category.save()

def get_top_categories():
    top_categories = Category.objects.annotate(product_count=Count('products')).order_by('-product_count')[:3]
    context = []
    for category in top_categories:
        category_info = {
            'name': category.category_name,
            'description': category.description,
            'product_count': category.product_count
        }
        context.append(category_info)
    return context
    
