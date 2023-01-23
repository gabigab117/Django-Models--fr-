from django.shortcuts import render

from blog.models import BlogPost


def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/post.html", context={"blog_post": post})

