from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView

from website.forms import SignupForm
from blog.models import BlogPost
from django.views import View

'''
# on va utiliser une vue fondée sur une class, une vue toute simple
class HomeView(View):
    title = "Default"

    # méthode qui va procésser les requetes get
    def get(self, request):
        return HttpResponse(f"<h1>{self.title}</h1><br><a href='/blog/'> Le Blog</a>")
'''


# avec un templateview on peut retourner un template html
class HomeView(TemplateView):
    template_name = "website/indexclass.html"
    title = "Default"

    # modifier le contexte :
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


'''
def blog_posts(request):

    # je peux créer une instance de HttpResponse
    # inspecter les outils de dev de Edge pour voir ce qu'il se passe
    r = HttpResponse()
    # r.content = "Bonjour tout le monde"
    r.content = "{'1': 'Bonjour tout le monde'}"
    # on peut très bien changer le status code mais la requête va tt de mm fonctionner.
    r.status_code = 404
    # l'objet est comme un dictionnaire, ci-dessous on ne retourne plus txt HTML mais app json
    r['Content-Type'] = 'application/json'
    return r
'''

'''
def blog_posts(request):
    json_response = JsonResponse({"1": "Premer article du blog"})
    json_response.status_code = 202
    return json_response
    # return JsonResponse({"1": "Premier article du blog"})

'''


def blo_posts(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    # on affiche le contenu de l'article si on a réussi à le récupérer
    return render(request, "website/test.html", context={"blog_post": blog_post})


# variables et conditions (gabarit)
def blo_posts_gabarit(request):
    posts = BlogPost.objects.filter(pk__in=[1, 2])

    return render(request, "website/gabarit.html", context={"posts": posts})


# boucles (gabarit)
def blo_posts_gabarit_boucle(request):
    posts = BlogPost.objects.all()
    users = User.objects.all()
    return render(request, "website/gabaritboucle.html", context={"posts": posts, "users": users})


# def blog_posts_redirect(request):
# on récupère le name de notre url
# je peux faire redirect("https://google.fr") par exemple
# return redirect("home")


@login_required
def view_login(request):
    return HttpResponse("<h1>Vous devez être connecté pour voir ça</h1>")


# @user_passes_test(lambda u: u.username == "gabri")
# lambda argument: expression
@user_passes_test(lambda u: "Modérateurs" in [group.name for group in u.groups.all()])
def view_login_cond(request):
    return HttpResponse("<h1>Restreindre avec une condition</h1>")


# vue formulaire signup
def signup(request):
    # récupérer les données d'un formulaire (.html) dans la vue:
    # quel type de méthode effectuée par la request
    if request.method == "POST":
        # si method est type POST, on récupère les données envoyées dans la variable POST
        # POST = dictionnaire qui contient les données qui sont envoyées avec la requête POST
        # je passe donc un dictionnaire (qui correspond aux données du formulaire) à la class SignupForm
        form = SignupForm(request.POST)
        # on vérifie que le formulaire est valide

        if form.is_valid():
            # retourne le dictionnaire avec les données nettoyées
            # il faut tjs vérifier avec is valid si je veux afficher les clean data
            print(form.cleaned_data)
            return HttpResponse("Merci de vous êtes....")

    else:
        # créer une instance (formulaire vide)
        form = SignupForm()

    # on passe à notre vue le formulaire vide avec else, mais si la méthode POST a été utilisée,
    # l'utilisateur ne perd pas les données entrées si le is_valid est false
    return render(request, "accounts/signup.html", context={"form": form})


'''
def email_check(user):
    return user.email.endswith('@example.com')

@user_passes_test(email_check)
def my_view(request):
'''
