from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    index,
    CatalogListView,
    CatalogDetailView,
    CatalogCreateView,
    ContactsView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("catalog", CatalogListView.as_view(), name="catalog"),
    path("contacts", ContactsView.as_view(), name="contacts"),
    path("product_item/<int:pk>", CatalogDetailView.as_view(), name="product_item"),
    path("new_product", CatalogCreateView.as_view(), name="new_product"),
]
