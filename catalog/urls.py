from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", catalog, name="catalog"),
    path("contacts", contacts, name="contacts")
]
