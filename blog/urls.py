from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("article/<int:pk>", BlogDetailView.as_view(), name="article"),
    path("new_article", BlogCreateView.as_view(), name="new_article"),
    path("edit_article/<int:pk>", BlogUpdateView.as_view(), name="edit_article"),
    path("delete_article/<int:pk>", BlogDeleteView.as_view(), name="delete_article"),
]
