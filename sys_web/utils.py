
## chamar ela colocando em uma lista pra ser usada na lista de pesos
def normalizar(lista_elementos):
    lista_final_normalizada = []
    lista_dos_somados = []
    lista_normalizada = []
    lista_sem_zero = []
    for elemento in lista_elementos:
        soma = sum(elemento)
        lista_dos_somados.append(soma)
    
    for elemento_da_soma in lista_dos_somados:
        maior , menor = max(lista_dos_somados), min(lista_dos_somados)
        if maior == menor:
            regular = 0
        else:
            regular = ((elemento_da_soma - menor)/(maior - menor))
        lista_normalizada.append(regular)
    
    for i in lista_normalizada:
        if i > 0:
            lista_sem_zero.append(i)

    for elemento_normalizado in lista_normalizada:
        if elemento_normalizado > 0:
            lista_final_normalizada.append(elemento_normalizado)
        else:
            menor_zero = min(lista_sem_zero)
            lista_final_normalizada.append(menor_zero*0.01)


    return lista_final_normalizada

#chamar dentro de uma lista pra ser usada 
def normalizar_alternativas(lista_elementos):
    lista_dos_somados = []
    lista_normalizada = []
    
    for elemento in lista_elementos:
        soma = sum(elemento)
        lista_dos_somados.append(soma)
    
    for elemento_da_soma in lista_dos_somados:
        maior , menor = max(lista_dos_somados), min(lista_dos_somados)
        if maior == menor :
            regular = 0
        else:
            regular = ((elemento_da_soma - menor)/(maior - menor))
        lista_normalizada.append(regular)
    
    return lista_normalizada


def peso_criterios(lista_elementos):
    num_elementos = len(lista_elementos) -1
    pesos = []
    i = 0
    while i <= num_elementos:
        soma = sum([item[i] for item in lista_elementos])
        i =  i + 1
        pesos.append(soma)
    return pesos

##ela vem uma lista de listas de todas as alternativas normalizadas por cada criterio
def soma_alternativa_por_criterio(lista_elementos):
    num_elementos = len(lista_elementos) -1
    lista_somada = []
    i = 0
    while i <= num_elementos:
        soma = sum([item[i] for item in lista_elementos])
        i =  i+ 1
        lista_somada.append(soma)
    return lista_somada

def multiplica_final(lista_elementos, lista_pesos):
    num_elementos = len(lista_pesos) 

    lista_somada = []
 
    i = 0
    while i < num_elementos:
        lista_primeiros_elementos = []
        lista_primeiros_elementos = [item[i] for item in lista_elementos]
        lista_multi = []

        for numint, peso in enumerate(lista_pesos):
            multi = peso * lista_primeiros_elementos[numint]
            lista_multi.append(multi)


        i =  i + 1
        lista_somada.append(sum(lista_multi))
    return lista_somada    