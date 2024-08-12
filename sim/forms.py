from django import forms

class EntryForm(forms.Form):
    prenom = forms.CharField(max_length=100)
    telephone = forms.CharField(max_length=15)
    lieu_naissance = forms.CharField(max_length=100)
    Actue = forms.CharField(max_length=100)
