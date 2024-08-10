from django import forms
from catalog.models import Products


class CatalogCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = (
            "view_count",
            "slug",
        )
