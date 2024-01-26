from django import forms
from .models import Profil


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['photo', 'age']
