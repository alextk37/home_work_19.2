from django.shortcuts import render
from catalog.models import Category, Products, Version
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
)
from django.urls import reverse_lazy
from catalog.forms import (
    CatalogCreateForm,
    VersionForm,
    CatalogUpdateForm,
    ModeratorUpdateForm,
)
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from config.cached import get_cached


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

    def get_queryset(self):
        # Получаем все продукты, у которых есть активные версии
        return Products.objects.prefetch_related("versions").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем активные версии для всех продуктов
        active_versions = Version.objects.filter(is_active=True)

        # Создаем словарь для хранения активных версий по продуктам
        version_dict = {}
        for version in active_versions:
            version_dict[version.product.id] = version.version

        # Добавляем номер версии в контекст для каждого продукта
        for product in context["products"]:
            product.current_version = version_dict.get(product.id)

        context["title"] = "Каталог"
        return context


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


class CatalogFormMixin:
    template_name = "new_product.html"

    def get_success_url(self):
        return reverse_lazy("catalog:catalog")


class CatalogCreateView(CatalogFormMixin, CreateView, LoginRequiredMixin):
    model = Products
    form_class = CatalogCreateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Products, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)

        context_data["title"] = "Новый продукт"
        return context_data

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.user = user
        product.save()

        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class CatalogUpdateView(CatalogFormMixin, UpdateView):
    model = Products

    def get_form_class(self):
        if self.request.user.groups.filter(name="Moderator").exists():
            return ModeratorUpdateForm
        else:
            return CatalogUpdateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Products, Version, form=VersionForm, extra=0
        )
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)

        context_data["title"] = "Изменение продукта"
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        self.object = form.save()
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context


def category_list_view(request):
    categories = get_cached(Category, 600)

    return render(request, "categories.html", {"categories": categories})
