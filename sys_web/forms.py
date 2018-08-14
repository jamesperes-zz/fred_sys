from django import forms
from django.forms import (formset_factory, modelformset_factory)

from .models import *


class DecisorForm(forms.Form):
    name = forms.CharField(
        label='Decisor name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Decisor name'
        })
    )


class DecisorModelForm(forms.ModelForm):

    class Meta:
        model = Decisor
        fields = ('name', )
        labels = {
            'name': 'Decisor name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Decisor name'
                }
            )
        }


DecisorFormset = formset_factory(DecisorForm)
DecisorModelFormset = modelformset_factory(
    Decisor,
    fields=('name', ),
    extra=1,
    widgets={
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Decisor name'
            }
        )
    }
)


class CriterioForm(forms.Form):
    name = forms.CharField(
        label='Criterio nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Criterio Nome'
        })
    )


class CriterioModelForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = ('name', )
        labels = {
            'name': 'Criterio nome'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Criterio nome'
                }
            )
        }

CriterioFormset = formset_factory(CriterioForm)
CriterioModelFormset = modelformset_factory(
    Criterio,
    fields=('name', ),
    extra=1,
    widgets={
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Criterio nome'
            }
        )
    }
)


class AlternativaForm(forms.Form):
    name = forms.CharField(
        label='Alternativa name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Alternativa name'
        })
    )


class AlternativaModelForm(forms.ModelForm):

    class Meta:
        model = Alternativa
        fields = ('name', )
        labels = {
            'name': 'Alternativa name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Alternativa name'
                }
            )
        }


AlternativaFormset = formset_factory(AlternativaForm)
AlternativaModelFormset = modelformset_factory(
    Alternativa,
    fields=('name', ),
    extra=1,
    widgets={
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Alternativa name'
            }
        )
    }
)



