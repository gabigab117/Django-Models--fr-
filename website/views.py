from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required

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


def blog_posts(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    # on affiche le contenu de l'article si on a réussi à le récupérer
    return render(request, "website/test.html", context={"blo_post": blog_post})


def blog_posts_redirect(request):
    # on récupère le name de notre url
    # je peux faire redirect("https://google.fr") par exemple
    return redirect("home")


@login_required
def view_login(request):
    return HttpResponse("<h1>Vous devez être connecté pour voir ça</h1>")
