from django.db import models


# Create your models here.
class BlogPost(models.Model):
    # pour CharField il faut absolument définir une longueur en param
    title = models.CharField(max_length=100)
    # pour transformer title en url on utilise un slug
    slug = models.SlugField()
    # valeur par défaut en param
    published = models.BooleanField(default=False)
    # blank permet de spécifier que je peux laisser vide. Sinon obligé de renseigner date
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()
