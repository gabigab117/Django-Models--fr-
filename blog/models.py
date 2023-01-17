from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()


class BlogPost(models.Model):
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

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
