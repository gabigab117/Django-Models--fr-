from django.shortcuts import render

from blog.models import BlogPost


def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    lowlow = post.title.lower()
    return render(request, "blog/post.html", context={"blog_post": post, "lowlow": lowlow})


def echappement(request):
    # ici le javascript devrait ouvrir une popup. Mais Django gère l'échappement
    name = "<script>alert('HelloWorld')</script>"

    return render(request, "blog/echappement.html", context={"name": name})


def etendre(request):

    return render(request, "blog/etendre.html")


def etendu(request):
    posts = BlogPost.objects.all()

    return render(request, "blog/etendu.html", context={"posts": posts})


def etendupost(request, pk):
    post = BlogPost.objects.get(pk=pk)

    return render(request, "blog/etendupost.html", context={"post": post})
