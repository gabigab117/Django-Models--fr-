from django.urls import path
from blog.views import blog_post, blog_posts

urlpatterns = [
    path('', blog_posts, name="blog-index"),
    path('<str:slug>/', blog_post, name="blog-post"),
]