from django import forms
from catalog.models import Products
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


class CatalogCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ("product_name", "description", "preview_img", "category", "price")

    def clean_product_name(self):
        cleaned_data = super().clean()["product_name"]

        if cleaned_data in STOP_WORDS:
            raise ValidationError("Недопустимое имя продукта")
        else:
            return cleaned_data
