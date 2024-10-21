from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    index,
    CatalogListView,
    CatalogDetailView,
    CatalogCreateView,
    ContactsView,
    CatalogUpdateView,
    category_list_view
)
from  django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("catalog", CatalogListView.as_view(), name="catalog"),
    path("contacts", ContactsView.as_view(), name="contacts"),
    path("product_item/<int:pk>", cache_page(600)(CatalogDetailView.as_view()), name="product_item"),
    path("new_product", CatalogCreateView.as_view(), name="new_product"),
    path("update_product/<int:pk>", CatalogUpdateView.as_view(), name="update_product"),
    path("categories/", category_list_view, name='category_list' )]
