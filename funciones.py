
def mostrar_mensaje(mensaje:str):
    print("{0}".format(mensaje))

def es_numero(cadena:str):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
    
'''Ésta funcion ROBADA verifica si el str que se le pasa es un número.'''

def mostrar_diccionario(diccionario: dict, *claves: str):
    for clave in claves:
        if clave in diccionario:
            valor = diccionario[clave]
            if es_numero(valor):
                valor = "{:.2f}".format(float(valor))
            print("{0}: {1}".format(clave, valor))

'''Función que imprime un diccionario con multiples claves que se deben pasar en los parametros, corroborara si el 
str que se le pasa es un número, en dicho caso lo hará un flotante y lo mostrará con 2 decimales.'''

def mostrar_lista(lista:list, *claves:str):
    if len(lista) > 0:
        for elemento in lista:
            mostrar_diccionario(elemento, *claves)
    else:
        print("La lista está vacía")

'''Función que verifica si una lista está vacía, en caso de no estarlo, la recorre y muestra sus valores recurriendo
a la función mostrar_diccionario, de lo contrario, imprime un mensaje que la lista está vacía.'''

def calcular_maximo_minimo_lista(lista: list, clave: str, tipo: str) -> dict:
    retorno = None
    if len(lista) > 0:
        max_min = lista[0]
        for elemento in lista:
            elemento_valor = float(elemento[clave])
            max_min_valor = float(max_min[clave])
            if tipo == "minimo" and elemento_valor < max_min_valor:
                max_min = elemento
            if tipo == "maximo" and elemento_valor > max_min_valor:
                max_min = elemento
        retorno = max_min
    return retorno

'''Ésta función calcula el máximo o el mínimo de un elemento en una lista, recibe como parametros la lista,
la clave y el tipo (maximo o minimo) en caso de que la lista se encuentre vacia devolverá un -1.'''

def calcular_promedio_lista(lista:list, clave:str) -> float or bool:   
    suma = 0
    retorno = False
    if lista != []:
        for elemento in lista:
            elemento[clave] = float(elemento[clave])
            suma += elemento[clave]
            promedio = suma / len(lista)
            retorno = promedio
    return  retorno

'''Esta función calcula un promedio de una lista, recibiendo como parametros la lista y la clave del elemento
que queremos el promedio.'''

def mostrar_promedio(clave_0:str, promedio:float, clave_2:str):
    print("El promedio de {0} es {1:.2f} {2}".format(clave_0, promedio, clave_2))

def crear_lista_solicitada(lista:list, clave:str, valor_deseado:str) -> list:
    lista_solicitada = []
    for elemento in lista:
        if elemento[clave] == valor_deseado:
            lista_solicitada.append(elemento)
    return lista_solicitada

''' Ésta función solicita una lista, una clave y un valor deseado para devolver una lista que contendra
los diccionarios que contengan el valor deseado de la primera lista. Es decir, funciona como un filtro 
que crea una nueva lista en base a una lista original.'''

def contar_datos_lista(lista: list, clave: str) -> dict:
    diccionario_contador = {}
    for elemento in lista:
        if elemento[clave] in diccionario_contador:
            diccionario_contador[elemento[clave]] += 1
        else:
            diccionario_contador[elemento[clave]] = 1
    return diccionario_contador

'''Ésta función crea un diccionario vacio, luego recorre la lista que se le es pasada por parametro
buscando de, los elementos de la lista, el que tenga la clave especificada y lo añade al diccionario que devolvera.
 En caso de que la clave ya se encuentre en el diccionario, sumará +1 a esa clave, si no, añadirá la clave nueva
 al diccionario.'''

def agrupar_lista_por_parametro(lista:list, clave:str) -> dict:
    diccionario = {}
    for elemento in lista:
        valor_clave = elemento[clave]
        if valor_clave in diccionario:
            diccionario[valor_clave].append(elemento)
        else:
            diccionario[valor_clave] = [elemento]
    return diccionario

'''Esta función recibe como parametro una lista, el segundo parametro la clave que utilizará para agrupar
y como tercer parametro el dato que será guardado como valor en el diccionario que retornará.'''