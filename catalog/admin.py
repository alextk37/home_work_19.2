from django.contrib import admin

from catalog.models import Category, Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")
    search_fields = ("category_name",)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "price", "category")
    search_fields = ("product_name", "description")
    list_filter = ("category",)
