from django import forms
from catalog.models import Products, Version
from django.core.exceptions import ValidationError

STOP_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class FormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            print(field_name)
            if field_name == "is_active":
                field.widget.attrs["class"] = "form-check-input"

    def clean_product_name(self):
        cleaned_data = super().clean()["product_name"]

        if cleaned_data in STOP_WORDS:
            raise ValidationError("Недопустимое имя продукта")
        else:
            return cleaned_data


class CatalogCreateForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            "product_name",
            "description",
            "preview_img",
            "category",
            "price",
            "is_published",
        )


class CatalogUpdateForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Products
        fields = ("product_name", "description", "preview_img", "category", "price")


class ModeratorUpdateForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            "is_published",
            "description",
            "category",
        )


class VersionForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ("version", "name_version", "is_active")
