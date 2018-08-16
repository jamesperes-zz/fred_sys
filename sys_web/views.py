from django.shortcuts import render, redirect
from django.views import generic
from itertools import combinations

from .forms import *
from .models import *
from .utils import *


def home(request):
    template_name = 'sys_web/home.html'
    heading_message = 'Decisores'
    if request.method == "POST":
        form_decisor = DadosForm(request.POST)
        if form_decisor.is_valid():
            decisor_conteudo = form_decisor.save()
            return redirect("avaliacriterios")


    return render(request, template_name, {'heading': heading_message})


def avaliacriterios(request):
    template_name = 'sys_web/avaliacriterios.html'
    heading_message = 'Decisores'
    dados = Dados.objects.order_by('-pk')[0]
    if request.method == "POST":
        form_decisor = CriteriosForm(request.POST)
        if form_decisor.is_valid():
            decisor_conteudo = form_decisor.save()
            return redirect("avaliarum")

    return render(request, template_name, {'heading': heading_message, 'dados':dados})

def avaliarum(request):
    template_name = 'sys_web/avaliarum.html'

    dados = Dados.objects.order_by('-pk')[0]
    heading_message = dados.decisor1
    if request.method == "POST":
        form_decisor = AvaliarumForm(request.POST)
        if form_decisor.is_valid():
            decisor_conteudo = form_decisor.save()
            return redirect("avaliardois")

    return render(request, template_name, {'heading': heading_message, 'dados':dados})

def avaliardois(request):
    template_name = 'sys_web/avaliardois.html'

    dados = Dados.objects.order_by('-pk')[0]
    heading_message = dados.decisor2
    if request.method == "POST":
        form_decisor = AvaliardoisForm(request.POST)
        if form_decisor.is_valid():
            decisor_conteudo = form_decisor.save()
            return redirect("avaliartres")

    return render(request, template_name, {'heading': heading_message, 'dados':dados})

def avaliartres(request):
    template_name = 'sys_web/avaliartres.html'

    dados = Dados.objects.order_by('-pk')[0]
    heading_message = dados.decisor3
    if request.method == "POST":
        form_decisor = AvaliartresForm(request.POST)
        if form_decisor.is_valid():
            decisor_conteudo = form_decisor.save()
            return redirect("resultado")

    return render(request, template_name, {'heading': heading_message, 'dados':dados})


def resultado(request):
    template_name = 'sys_web/resultado.html'
    heading_message = "Resultado"
    dados = Dados.objects.order_by('-pk')[0]
    cr = Criterios.objects.order_by('-pk')[0]
    a_um = Avaliarum.objects.order_by('-pk')[0]
    a_do = Avaliardois.objects.order_by('-pk')[0]
    a_tr = Avaliartres.objects.order_by('-pk')[0]


    peso_decisor_um = normalizar([[0, cr.d1c1c2, cr.d1c1c3],[cr.d1c1c2*-1,0,cr.d1c2c3],[cr.d1c1c3*-1,cr.d1c2c3*-1,0]])
    peso_decisor_dois = normalizar([[0, cr.d2c1c2, cr.d2c1c3],[cr.d2c1c2*-1,0,cr.d2c2c3],[cr.d2c1c3*-1,cr.d2c2c3*-1,0]])
    peso_decisor_tres = normalizar([[0, cr.d3c1c2, cr.d3c1c3],[cr.d3c1c2*-1,0,cr.d3c2c3],[cr.d3c1c3*-1,cr.d3c2c3*-1,0]])

    peso_final = peso_criterios([peso_decisor_um, peso_decisor_dois, peso_decisor_tres])
  

    aval_um_c1 = normalizar_alternativas([[0,a_um.c1a1a2, a_um.c1a1a3],[a_um.c1a1a2*-1, 0, a_um.c1a2a3],[a_um.c1a1a3*-1, a_um.c1a2a3*-1,0]])
    aval_um_c2 = normalizar_alternativas([[0,a_um.c2a1a2, a_um.c2a1a3],[a_um.c2a1a2*-1, 0, a_um.c2a2a3],[a_um.c2a1a3*-1, a_um.c2a2a3*-1,0]])
    aval_um_c3 = normalizar_alternativas([[0,a_um.c3a1a2, a_um.c3a1a3],[a_um.c3a1a2*-1, 0, a_um.c3a2a3],[a_um.c3a1a3*-1, a_um.c3a2a3*-1,0]])


    aval_do_c1 = normalizar_alternativas([[0,a_do.c1a1a2, a_do.c1a1a3],[a_do.c1a1a2*-1, 0, a_do.c1a2a3],[a_do.c1a1a3*-1, a_do.c1a2a3*-1,0]])
    aval_do_c2 = normalizar_alternativas([[0,a_do.c2a1a2, a_do.c2a1a3],[a_do.c2a1a2*-1, 0, a_do.c2a2a3],[a_do.c2a1a3*-1, a_do.c2a2a3*-1,0]])
    aval_do_c3 = normalizar_alternativas([[0,a_do.c3a1a2, a_do.c3a1a3],[a_do.c3a1a2*-1, 0, a_do.c3a2a3],[a_do.c3a1a3*-1, a_do.c3a2a3*-1,0]])


    aval_tr_c1 = normalizar_alternativas([[0,a_tr.c1a1a2, a_tr.c1a1a3],[a_tr.c1a1a2*-1, 0, a_tr.c1a2a3],[a_tr.c1a1a3*-1, a_tr.c1a2a3*-1,0]])
    aval_tr_c2 = normalizar_alternativas([[0,a_tr.c2a1a2, a_tr.c2a1a3],[a_tr.c2a1a2*-1, 0, a_tr.c2a2a3],[a_tr.c2a1a3*-1, a_tr.c2a2a3*-1,0]])
    aval_tr_c3 = normalizar_alternativas([[0,a_tr.c3a1a2, a_tr.c3a1a3],[a_tr.c3a1a2*-1, 0, a_tr.c3a2a3],[a_tr.c3a1a3*-1, a_tr.c3a2a3*-1,0]])


    soma_alte_c1 = soma_alternativa_por_criterio([aval_um_c1, aval_do_c1, aval_tr_c1])
    soma_alte_c2 = soma_alternativa_por_criterio([aval_um_c2, aval_do_c2, aval_tr_c2])
    soma_alte_c3 = soma_alternativa_por_criterio([aval_um_c3, aval_do_c3, aval_tr_c3])



    resultado_um = multiplica_final([soma_alte_c1, soma_alte_c2, soma_alte_c3], peso_final)
    resultado = [(dados.alternativa1,resultado_um[0]),(dados.alternativa2,resultado_um[1]), (dados.alternativa3,resultado_um[2])]

    resultado.sort(key=lambda x: x[1] ,reverse=True)


    return render(request, template_name, {'heading': heading_message, 'dados':dados, 'resultado':resultado, 'peso_final':peso_final})