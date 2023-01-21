from django.urls import path
from blog.views import blog_post

urlpatterns = [
    path('<str:slug>/', blog_post, name="blog-post"),
]