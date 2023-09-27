from data_stark import *
from stark_2 import *

while True:
    menu = (
'''A. Mostrar superheroes de género no binario.
B. Mostrar superheroe más alto de género femenino.
C. Mostrar superheroe más alto de género masculino.
D. Mostrar superheroe más débil de género masculino.
E. Mostrar superheroe más débil de género no binario.
F.Mostrar promedio de fuerza de superheroes género no binario.
G. Mostrar colores de ojos y cantidad de heroes que lo poseen.
H. Mostrar colores de pelo y cantidad de heroes que lo poseen.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia.
K. SALIR de S.T.A.R.K II''')   
    print(menu)
    opcion = input("Ingrese una opción: ")

    if opcion == "A" or opcion == "a":
        mostrar_heroes_nb()
    elif opcion == "B" or opcion == "b":
        mostrar_superheroina_mas_alta()
    elif opcion == "C" or opcion == "c":
        mostrar_superheroe_mas_alto()
    elif opcion == "D" or opcion == "d":
        mostrar_heroe_mas_debil()
    elif opcion == "E" or opcion == "e":
        mostrar_heroe_nb_mas_debil()
    elif opcion == "F" or opcion == "f":
        mostrar_promedio_fuerza_heroes_nb()
    elif opcion == "G" or opcion == "g":
        mostrar_color_ojos()
    elif opcion == "H" or opcion == "h":
        mostrar_color_pelo()
    elif opcion == "I" or opcion == "i":
        heroes_por_color_ojos()
    elif opcion == "J" or opcion == "j":
        heroes_por_tipo_inteligencia()
    elif opcion == "K" or opcion == "k":
        print("Gracias por usar S.T.A.R.K II")
        break

    else:
        print("Introduce una opción valida.")

'''Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia

"nombre": "Rocket Raccoon",
    "identidad": "Rocket Raccoon",
    "empresa": "Marvel Comics",
    "altura": "122.77",
    "peso": "25.73",
    "genero": "NB",
    "color_ojos": "Brown",
    "color_pelo": "Brown",
    "fuerza": "5",
    "inteligencia": "average"'''
  

