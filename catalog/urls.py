from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts, index

app_name = CatalogConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("catalog", catalog, name="catalog"),
    path("contacts", contacts, name="contacts")
]
