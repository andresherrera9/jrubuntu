from django import forms
from .models import entidad_opcion
from django.forms import ModelForm
from django.forms.widgets import NumberInput




ENTIDADES_CHOICES = [
    ('banco a','Banco A'),
    ('banco b', 'Banco B'),
    ('banco c','Banco C'),
]


DOCUMENTOS_SOLICITUD = [
    ('exogenas','Exogenas'),
    ('renta','Renta'),
    ('etc','Etc'),
]

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

#class solicitudForm(ModelForm):
#    class Meta:
#        model = entidad_opcion
#        fields = ['entidad','opcion']

class solicitudForm(forms.Form):

    entidad = forms.ChoiceField( label='Entidad a solicitar:',choices=ENTIDADES_CHOICES)

    documentos = forms.MultipleChoiceField(label='Escoja documentos',choices=DOCUMENTOS_SOLICITUD, required = True, widget=forms.CheckboxSelectMultiple)

    texto = forms.CharField(widget=forms.Textarea, label="Dejanos un comentario", required = False)

    fecha_i = forms.DateField(widget=NumberInput(attrs={'type':'date'}), label='Fecha inicial')

    fecha_f = forms.DateField(widget=NumberInput(attrs={'type':'date'}), label='Fecha final')

    #DOCUMENTOS = forms.MultipleChoiceField(
    #    required = False,
    #    widget = forms.CheckboxSelectMultiple,
    #    choices = DOCUMENTOS_SOLICITUD,
    #)