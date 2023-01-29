from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required, user_passes_test

from website.forms import SignupForm
from blog.models import BlogPost


def home(request):
    return HttpResponse("<h1>Accueil ! ! !</h1>")


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
        # je passe donc un dictionnaire à la class SignupForm
        form = SignupForm(request.POST)
        # on vérifie que le formulaire est valide

        if form.is_valid():
            # retourne le dictionnaire avec les données nettoyées
            print(form.cleaned_data)

    # créer une instance
    form = SignupForm()
    return render(request, "accounts/signup.html", context={"form": form})


'''
def email_check(user):
    return user.email.endswith('@example.com')

@user_passes_test(email_check)
def my_view(request):
'''
