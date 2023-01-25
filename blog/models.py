from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Toutes les catégories"

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    # on va relier User à BlogPost (relations plusieurs à 1) avec une foreign key
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # pour le plusieurs à plusieurs Pas besoin de spécifier le on_delete ==>
    category = models.ManyToManyField(Category)
    # pour CharField il faut absolument définir une longueur en param
    title = models.CharField(max_length=100)
    # pour transformer title en url on utilise un slug
    slug = models.SlugField(blank=True)
    # valeur par défaut en param
    published = models.BooleanField(default=False)
    # blank permet de spécifier que je peux laisser vide. Sinon obligé de renseigner date
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    # une info que je ne veux pas forcémment stocker dans ma BDD mais juste afficher ==>
    def publish_string(self):
        if self.published:
            return "L'article est publié"
        return "L'article est inaccessible"

    @property
    def number_of_words(self):
        return len(self.content.split())

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Tous les articles"
        # ordonner en fonction de la date, utiliser le champs date ==>
        # si on fait ["-date"] on inverse l'ordre
        ordering = ["-date", "-published"]

    def __str__(self):
        # self car je veux retourner le titre des instances
        return f"{self.title} - {self.date}"

    # depuis mon instance si je veux la voir dans le site (bouton voir sur le site)
    def get_absolute_url(self):
        # name de mon url, et élément kwargs que l'on passe à notre url. Ici dans l'url <str:slug>
        return reverse("blog-post", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # ici la condition est avant mon super, car on souhaite modifier les slug avant la save
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
