from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='list'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/<str:slug>', BlogDetailView.as_view(), name='detail_blog'),
    path('blog/edit/<str:slug>', BlogUpdateView.as_view(), name='edit_blog'),
    path('blog/delete/<str:slug>', BlogDeleteView.as_view(), name='delete_blog'),
]
