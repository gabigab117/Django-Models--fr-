from django import forms

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        # je peux tout faire apparaitre avec fields = "__all__"
        fields = [
            "title",
            "author",
            "date",
            "category",
            "description"
        ]
        # modifier les champs
        labels = {
            "title": "Titre",
            "category": "Catégorie"
        }
        widgets = {"date": forms.SelectDateWidget(years=range(1990, 2040))}
