from django.urls import path
from blog.views import blog_post, blog_posts, echappement, etendre, etendu, etendupost, blog_post_form

urlpatterns = [
    path('', blog_posts, name="blog-index"),
    path('echap/', echappement, name="echap"),
    path('etendre/', etendre, name="etendre-template"),
    path('etendu/', etendu, name="template-etendu"),
    path('post-pk<str:pk>/', etendupost, name="etendu-post"),
    path('post-<str:slug>/', blog_post, name="blog-post"),

    # ci-dessous urls pour les forms
    path('article/', blog_post_form, name="blog-post-form")
]