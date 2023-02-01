"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website.views import blo_posts, view_login, view_login_cond, blo_posts_gabarit, blo_posts_gabarit_boucle, signup
from website.views import HomeView


# attention à l'odre des chemins, si on met le <str:slug> en premier django ne s'occupera pas de blog/, loginview/...
urlpatterns = [
    # home, vue fondée sur les class. importer HomeView, puis initialiser avec méthode as_view() (on créer une instance)
    # 1 vue simple :
    # path('', HomeView.as_view(title="Accueil du site"), name="home"),
    # avec la même class mais une autre instance en modifiant l'attribut de la class
    # path('about/', HomeView.as_view(title="A propos"), name="about"),
    # 2 vue template view
    path('', HomeView.as_view(title="Accueil du site"), name="home"),
    path('about/', HomeView.as_view(title="A propos"), name="about"),
    # ---
    path('admin-secret/', admin.site.urls),
    # path('blog/', blog_posts_redirect, name="blog-index"),
    path('gabarit/', blo_posts_gabarit, name="gabarit"),
    path('gabaritboucle/', blo_posts_gabarit_boucle, name="gabarit-boucle"),
    path('loginview/', view_login, name="vue-login"),
    path('logincond', view_login_cond, name="login-condition"),
    path('blog/', include('blog.urls')),
    path('signup', signup, name="signup"),
    path('monslug<str:slug>/', blo_posts, name="blog-pasdanslapp"),

]
