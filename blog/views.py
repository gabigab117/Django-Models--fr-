from django.shortcuts import render
from blog.models import BlogPost
from blog.forms import BlogPostForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView


def blog_posts(request):
    posts = BlogPost.objects.all()
    # ou
    posts2 = BlogPost.objects.filter(published=True)
    return render(request, "blog/index.html", context={"posts": posts})


# a la place de la vue basée sur la fonction blog_posts on va créer une class ListView
class BlogIndexView(ListView):
    # ci-dessous c'est comme si je faisais model = BlogPost.objects.all()
    # ca retourne tous nos objets dans notre context ds une variable object_list
    model = BlogPost
    # mais si je veux récupérer certains articles on ne fait pas model = BlogPost :
    # queryset = BlogPost.objects.filter(published=True)
    template_name = "blog/index_listview.html"
    # pour remplacer le nom de la variable object_list :
    context_object_name = "articles"


# on va récupérer un article
class BlogPostDetailView(DetailView):
    # ca retourne notre objet dans notre context ds une variable object
    model = BlogPost
    template_name = "blog/post_detailview.html"
    context_object_name = "post"
    # même pas besoin de passer en argument slug, on le passe dans l'url et django retrouve notre champs slug


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


# vue avec les forms
def blog_post_form(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)

        if form.is_valid():
            # je sauvegarde le formulaire avec form.save()
            # le paramètre commit=True par def. Donc si pas de param l'objet est sauvegardé dans la BDD
            # Avec commit=False je peux récupérer l'objet dans une variable pour le modifier
            # blog_post = form.save(commit=False)
            # blog_post.published = True
            # blog_post.save()
            # ou ne faire qu'un
            form.save()
            # donc sans variable car on ne récupère pas l'objet pour le modif
            # pour éviter de re-soumettre le formulaire :
            return HttpResponseRedirect(request.path)
            # path est un attribut qui correspond à l'url à laquelle je suis en train d'accéder
    else:
        # on va passer des valeurs initiales au formulaire
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = datetime.today()
        form = BlogPostForm(initial=init_values)

    return render(request, 'blog/postform.html', context={"form": form})
