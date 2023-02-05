from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from blog.models import BlogPost
from blog.forms import BlogPostForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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
            # ou ne faire qu'un form.save(), sinon
            form.instance.published = True
            if request.user.is_authenticated:
                form.instance.author = request.user
            form.save()
            # donc sans variable car on ne récupère pas l'objet pour le modif
            # pour éviter de re-soumettre le formulaire :
            # return HttpResponseRedirect(request.path)
            # path est un attribut qui correspond à l'url à laquelle je suis en train d'accéder
            return HttpResponseRedirect(reverse("blog-index"))
    else:
        # on va passer des valeurs initiales au formulaire
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = datetime.today()
        form = BlogPostForm(initial=init_values)

    return render(request, 'blog/postform.html', context={"form": form})


# class createview pour utiliser le formulaire
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog/create_post.html"
    # ici on utilise les champs du modele :
    # fields = ['title', 'date', 'content']
    # on va plutot utiliser le formulaire lié à notre modèle
    form_class = BlogPostForm
    # pour rediriger vers une url
    # success_url = reverse_lazy("blog-index")
    # ou utiliser la méthode get_success_url

    def get_success_url(self):
        return reverse('blog-index')

    # modifier le formulaire avec une méthode form valid
    # la méthode suivante vérifie déjà si le formulaire est valide

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            # l'instance du BlogPost
            form.instance.author = self.request.user
        form.instance.published = True
        form.instance.date = datetime.today()
        # on a modifié notre formulaire puis on le retourne a form_valid avec super

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Créer"
        return context


# créer une vue d'édition
class BlogPostUpdateView(UpdateView):
    # pareil on spécifie le modèle, le template et quel form
    model = BlogPost
    template_name = "blog/create_post.html"
    form_class = BlogPostForm
    # on va modifier le context pour afficher modifier au lieu de créer dans le html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"
        return context


# vu pour supprimer une instance
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/delete_post.html"

    def get_success_url(self):
        # j'aurais pu faire un success_url = reverse_lazy
        return reverse('blog-index')
