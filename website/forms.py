from django import forms


class SignupForm(forms.Form):
    # ici je veux que quelqu'un puisse s'inscrire.
    JOBS = (
        # valeur BDD, valeur affichée
        ("python", "Développeur Python"),
        ("javascript", "Développeur javascript"),
        ("golang", "Développeur goalng")
    )
    # max_length, required sont des vérifications qui seront faites côté html.
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    # choices contient un tuple (ici JOBS) qui lui mm contient des tuples
    job = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect())
    cgu_accept = forms.BooleanField(initial=True)

    # on va créer une méthode pour faire des vérifications côté serveur
    # le nom de la méthode est toujours ainsi : clean_nomduchamps
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "*" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de *.")
        return pseudo
