from django import forms
from blog.models import Article


class FormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            print(field_name)
            if field_name == "is_active":
                field.widget.attrs["class"] = "form-check-input"


class ContentManagerForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description", "content", "preview_img"]


class ModeratorForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = ["is_published"]
