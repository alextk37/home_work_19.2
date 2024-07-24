from blog.models import Article
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Article
    template_name = "blog/blog.html"


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog/article.html"


class BlogCreateView(CreateView):
    model = Article
    template_name = "blog/new_article.html"
    fields = ["title", "description", "content", "preview_img"]
    success_url = reverse_lazy("blog:blog")


class BlogUpdateView(UpdateView):
    model = Article
    template_name = "blog/edit_article.html"
    fields = ["title", "description", "content", "preview_img"]
    success_url = reverse_lazy("blog:blog")


class BlogDeleteView(DeleteView):
    model = Article
    template_name = "blog/confirm.html"
    success_url = reverse_lazy("blog:blog")
