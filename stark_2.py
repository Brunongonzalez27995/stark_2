from funciones import *
from data_stark import *

def mostrar_heroes_nb():
    heroes_nb = crear_lista_solicitada(lista_personajes, "genero", "NB")
    mostrar_mensaje("Heroes de género no binario: ")
    mostrar_lista(heroes_nb, "nombre", "identidad")

def mostrar_superheroina_mas_alta():
    superheroes_mujeres = crear_lista_solicitada(lista_personajes, "genero", "F")
    heroina_mas_alta = calcular_maximo_minimo_lista(superheroes_mujeres, "altura", "maximo")
    mostrar_mensaje("Superheroina más alta: ")
    mostrar_diccionario(heroina_mas_alta, "nombre", "identidad")

def mostrar_superheroe_mas_alto():
    heroes_hombres = crear_lista_solicitada(lista_personajes, "genero", "M")
    heroe_mas_alto = calcular_maximo_minimo_lista(heroes_hombres, "altura", "maximo")
    mostrar_mensaje("Superheroe más alto: ")
    mostrar_diccionario(heroe_mas_alto, "nombre", "identidad")

def mostrar_heroe_mas_debil():
    heroes_hombres = crear_lista_solicitada(lista_personajes, "genero", "M")
    heroe_mas_debil = calcular_maximo_minimo_lista(heroes_hombres, "fuerza", "minimo")
    mostrar_mensaje("Superheroe masculino más debil: ")
    mostrar_diccionario(heroe_mas_debil, "nombre", "identidad")

def mostrar_heroe_nb_mas_debil():
    heroes_nb = crear_lista_solicitada(lista_personajes, "genero", "NB")
    heroe_nb_mas_debil = calcular_maximo_minimo_lista(heroes_nb, "fuerza", "minimo")
    mostrar_mensaje("Superheroe no binario más debil: ")
    mostrar_diccionario(heroe_nb_mas_debil, "nombre", "identidad")

def mostrar_promedio_fuerza_heroes_nb():
    heroes_nb = crear_lista_solicitada(lista_personajes, "genero", "NB")
    promedio = calcular_promedio_lista(heroes_nb, "fuerza")
    mostrar_promedio("fuerza de los heroes no binarios", promedio, ".")

def mostrar_color_ojos():
    cantidad_colores_de_ojos = contar_datos_lista(lista_personajes, "color_ojos")
    for color_ojos in cantidad_colores_de_ojos:
        cantidad = cantidad_colores_de_ojos[color_ojos]
        print("Color de ojos: {0} - Cantidad de héroes que lo tienen: {1}".format(color_ojos, cantidad))

def mostrar_color_pelo():
    cantidad_colores_de_pelo = contar_datos_lista(lista_personajes, "color_pelo")
    for color_pelo in cantidad_colores_de_pelo:
        cantidad = cantidad_colores_de_pelo[color_pelo]
        print("Color de pelo: {0} - Cantidad de héroes que lo tienen: {1}".format(color_pelo, cantidad))

def heroes_por_color_ojos():
    colores_ojos = agrupar_lista_por_parametro(lista_personajes, "color_ojos")
    for color_ojos, heroes in colores_ojos.items():
        print("Color de ojos: {0}\nHeroes que lo tienen: ".format(color_ojos))
        for heroe in heroes:
            print("- {0}".format(heroe["nombre"]))

def heroes_por_tipo_inteligencia():
    tipo_inteligencia = agrupar_lista_por_parametro(lista_personajes, "inteligencia")
    for inteligencia, heroes in tipo_inteligencia.items():
        print("Tipo de inteligencia: {0}\nHeroes con ésta inteligencia: ".format(inteligencia))
        for heroe in heroes:
            print("- {0}".format(heroe["nombre"]))

