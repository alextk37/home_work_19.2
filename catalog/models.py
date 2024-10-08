from django.db import models

NULLABLE = {"null": True, "blank": True}


class Products(models.Model):
    product_name = models.CharField(max_length=225, verbose_name="продукт")
    description = models.TextField(verbose_name="описание")
    preview_img = models.ImageField(
        upload_to="product_images", verbose_name="Изображение", **NULLABLE
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="категория"
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(
        verbose_name="Дата создания", auto_now=True, **NULLABLE
    )
    updated_at = models.DateField(
        verbose_name="Дата изменения", auto_now=True, **NULLABLE
    )
    # manufactured_at = models.DateField(verbose_name='Дата производства', **NULLABLE)
    view_count = models.IntegerField(verbose_name="Количество просмотров", default=0)
    slug = models.SlugField(max_length=255, unique=True, **NULLABLE)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        verbose_name="пользователь",
        **NULLABLE,
        related_name="products",
    )
    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("product_name",)
        permissions = [
            ("can_change_is_published", "Может редактировать статус публикации"),
            (
                "can_change_product_description",
                "Может редактировать количество описание",
            ),
            ("can_change_product_category", "Может редактировать категорию"),
        ]


class Category(models.Model):
    category_name = models.CharField(max_length=225, verbose_name="категория")
    description = models.TextField(verbose_name="описание")
    has_products = models.BooleanField(verbose_name="Есть продукты")

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("category_name",)


class Version(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        **NULLABLE,
        related_name="versions",
    )
    version = models.IntegerField(verbose_name="номер версии")
    name_version = models.CharField(
        verbose_name="имя версии", **NULLABLE, max_length=225
    )
    created_at = models.DateField(
        verbose_name="дата создания", auto_now=True, **NULLABLE
    )
    is_active = models.BooleanField(verbose_name="Активна", default=False)

    def __str__(self):
        return f"{self.version}"

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
        ordering = ("version",)
