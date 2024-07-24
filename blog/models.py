from django.db import models

NULLABLE = {"null": True, "blank": True}


class Article(models.Model):
    title = models.CharField(max_length=225, verbose_name="заголовок")
    description = models.TextField(verbose_name="описание")
    content = models.TextField(verbose_name="содержание")
    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)
    preview_img = models.ImageField(
        upload_to="article_images", verbose_name="Изображение", **NULLABLE
    )
    created_at = models.DateField(
        verbose_name="Дата создания", auto_now=True, **NULLABLE
    )
    updated_at = models.DateField(
        verbose_name="Дата изменения", auto_now=True, **NULLABLE
    )
    view_count = models.IntegerField(verbose_name="Количество просмотров", default=0)
    slug = models.SlugField(max_length=255, unique=True, **NULLABLE)

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ("title",)

    def __str__(self):
        return self.title
