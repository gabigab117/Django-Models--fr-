from django.urls import path
from blog.views import blog_post, blog_posts, echappement, etendre, etendu, etendupost, blog_post_form, BlogIndexView,\
    BlogPostDetailView

urlpatterns = [
    # path('', blog_posts, name="blog-index"),
    # url pour la vue ListViw qui remplace blog_posts ci-dessus, penser au as_view() pour créer l'instance
    path('', BlogIndexView.as_view(), name="blog-index"),
    path('echap/', echappement, name="echap"),
    path('etendre/', etendre, name="etendre-template"),
    path('etendu/', etendu, name="template-etendu"),
    path('post-pk<str:pk>/', etendupost, name="etendu-post"),
    # path('post-<str:slug>/', blog_post, name="blog-post"),
    # url pour DetailView qui remplace blog_post
    path('post-<str:slug>/', BlogPostDetailView.as_view(), name="blog-post"),

    # ci-dessous urls pour les forms
    path('article/', blog_post_form, name="blog-post-form")
]