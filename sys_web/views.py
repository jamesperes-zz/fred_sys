from django.shortcuts import render, redirect
from django.views import generic
from itertools import combinations

from .forms import *
from .models import *


def home(request):
    template_name = 'sys_web/home.html'
    heading_message = 'Decisores'
    if request.method == 'GET':
        formset = DecisorFormset(request.GET or None)
    elif request.method == 'POST':
        formset = DecisorFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Decisor(name=name).save()
            return redirect('criterios')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })

def criterios(request):
    template_name = 'sys_web/criterios.html'
    heading_message = 'Decisores'
    if request.method == 'GET':
        formset = CriterioFormset(request.GET or None)
    elif request.method == 'POST':
        formset = CriterioFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Criterio(name=name).save()
            return redirect('alternativas')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })

def alternativas(request):
    template_name = 'sys_web/alternativas.html'
    heading_message = 'Decisores'
    if request.method == 'GET':
        formset = AlternativaFormset(request.GET or None)
    elif request.method == 'POST':
        formset = AlternativaFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Alternativa(name=name).save()
            return redirect('home')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })

def avalia_criterios(request):
    criterios = Criterio.objects.all()
    decisores = Decisor.objects.all()
    criterios_combinados = combinations(criterios, 2)
    context = {"criterios": criterios_combinados, "decisores": decisores}
    return render(request, 'sys_web/avaliacriterios.html', context )

