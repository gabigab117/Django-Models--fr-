from django.contrib import admin
from .models import BlogPost, Category
# Register your models here.


# admin.site.register(BlogPost)
admin.site.register(Category)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # je pourrais spécifier des options ici
    # on va utiliser plusieurs attributs
    # list_display, un tuple avec nos champs sous forme de str
    list_display = (
        # avec les ManyToMany ça ne fonctionne pas
        "title",
        "published",
        "author",
        "date",
        "number_of_words",
    )

    # pour pouvoir éditer depuis l'admin où il y a toutes mes instances,
    # on utilise liste éditable, tjs mettre une virgule mm si on a qu'un champs.
    # on ne peut pas mettre le premier champs, car le premier champs est un lien vers mon instance.
    # sauf si on utilise ...
    list_editable = ("title", "published", )
    # ... list_display_links, ainsi la date est le lien vers mon instance et pas de pblm pour editer mon premier champs
    list_display_links = ("date", )
    # ! donc attention, on ne peut pas rendre editable un lien !

    # si je veux que les valeurs null affichent autre chose que - :
    empty_value_display = "Inconnu"

    # filtrer depuis la liste de mes instances, créer un tuple avec mes champs
    # dans le cas ci-dessous je filtre avec du txt
    search_fields = ("title", )

    # je veux filtrer en cliquant sur une valeur, pratique pour un booléen,
    # il ne faut pas mettre n'importe quel champs comme par exemple le content...
    # sinon on aura autant d'options que d'articles
    list_filter = ("published", "author", )

    # lorsque je modifie un article, je peux séléctionner un auteur dans une liste déroulante
    # si j'ai bcq d'auteur ça peut être compliqué, donc je vais ajouter une option de filtre avancé
    autocomplete_fields = ("author", )

    # pour un champs ManyToMany, on va utiliser un filtre horizontal :
    filter_horizontal = ("category", )

    # par défaut django affiche 100 instances (articles ici) par page dans l'admin
    # je peux modifier ça de cette façon :
    list_per_page = 3

