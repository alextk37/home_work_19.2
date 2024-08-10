from django.shortcuts import render
from catalog.models import Products
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
)
from django.urls import reverse_lazy
from catalog.forms import CatalogCreateForm


def index(request):
    context = {
        "top": Products.objects.all().order_by("-view_count")[:3],
        "title": "Главная",
    }
    return render(request, "index.html", context)


class CatalogListView(ListView):
    model = Products
    template_name = "catalog.html"
    context_object_name = "products"


class CatalogDetailView(DetailView):
    model = Products
    template_name = "product_item.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.product_name
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


class FormProductMixin:
    model = Products
    template_name = "new_product.html"
    form_class = CatalogCreateForm

    def get_success_url(self):
        return reverse_lazy("catalog:catalog")


class CatalogCreateView(FormProductMixin, CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новый продукт"
        return context


class CatalogUpdateView(FormProductMixin, UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактирование продукта"
        return context


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context
