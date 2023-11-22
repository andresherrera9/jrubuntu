from django import forms
from .models import Personas


class searchForm(forms.Form):
    searchTerm = forms.CharField(label='',max_length=100)