from django import forms
from django.forms import (formset_factory, modelformset_factory)

from .models import *


class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ("criterio1", "criterio2", "criterio3","decisor1", "decisor2", "decisor3","alternativa1", "alternativa2", "alternativa3",)


class CriteriosForm(forms.ModelForm):
    class Meta:
        model = Criterios
        fields = ("d1c1c2","d1c1c3","d1c2c3","d2c1c2","d2c1c3","d2c2c3","d3c1c2","d3c1c3","d3c2c3",)


class AvaliarumForm(forms.ModelForm):
    class Meta:
        model = Avaliarum
        fields = ("c1a1a2","c1a1a3","c1a2a3","c2a1a2","c2a1a3","c2a2a3","c3a1a2","c3a1a3","c3a2a3",)


class AvaliardoisForm(forms.ModelForm):
    class Meta:
        model = Avaliardois
        fields = ("c1a1a2","c1a1a3","c1a2a3","c2a1a2","c2a1a3","c2a2a3","c3a1a2","c3a1a3","c3a2a3",)


class AvaliartresForm(forms.ModelForm):
    class Meta:
        model = Avaliartres
        fields = ("c1a1a2","c1a1a3","c1a2a3","c2a1a2","c2a1a3","c2a2a3","c3a1a2","c3a1a3","c3a2a3",)


