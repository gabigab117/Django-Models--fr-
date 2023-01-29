from django import forms


class SignupForm(forms.Form):
    # ici je veux que quelqu'un puisse s'inscrire.
    JOBS = (
        # valeur BDD, valeur affichée
        ("python", "Développeur Python"),
        ("javascript", "Développeur javascript"),
        ("golang", "Développeur goalng")
    )
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    # choices contient un tuple (ici JOBS) qui lui mm contient des tuples
    job = forms.ChoiceField(choices=JOBS, widget=forms.SelectMultiple())
    cgu_accept = forms.BooleanField(initial=True)

