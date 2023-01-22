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
from website.views import blog_posts, home, blog_posts_redirect, view_login, view_login_cond


# attention à l'odre des chemins, si on met le <str:slug> en premier django ne s'occupera pas de blog/, loginview/...
urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('blog/', blog_posts_redirect, name="blog-index"),
    path('loginview/', view_login, name="vue-login"),
    path('logincond', view_login_cond, name="login-condition"),
    path('<str:slug>/', blog_posts, name="blog-pasdanslapp"),
    path('blog2/', include('blog.urls')),

]
