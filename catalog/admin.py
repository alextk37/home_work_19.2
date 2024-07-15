from django.contrib import admin

from catalog.models import Category, Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "has_products")
    search_fields = ("category_name",)
    list_filter = ("has_products",)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "price", "category")
    search_fields = ("product_name", "description")
    list_filter = ("category",)
