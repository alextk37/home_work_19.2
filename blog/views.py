from blog.models import Article
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.utils.text import slugify
from blog.forms import ContentManagerForm, ModeratorForm


class BlogListView(ListView):
    model = Article
    template_name = "blog/blog.html"

    def queryset(self):
        return Article.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Мой блог"
        return context


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog/article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Article
    template_name = "blog/new_article.html"
    fields = ["title", "description", "content", "preview_img", "is_published"]
    success_url = reverse_lazy("blog:blog")

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Article
    template_name = "blog/edit_article.html"

    def get_form_class(self):
        if self.request.user.groups.filter(name="ContentManager").exists():
            return ContentManagerForm
        else:
            return ModeratorForm

    def get_success_url(self):
        return reverse_lazy("blog:article", args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = Article
    template_name = "blog/confirm.html"
    success_url = reverse_lazy("blog:blog")
