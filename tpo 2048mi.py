import random
import os
import copy

def crear_tablero(fil):
    """ Crea una matriz con las filas y columnas con el valor q le pasemos"""
    tablero = []
    for i in range(fil):
        tablero.append([])
        for j in range(fil):
            tablero[i].append(0)
    return tablero

def mostrar_tablero(tablero):
    """ Crea copia tablero con espacios vacíos en vez de ceros y mustra copia """
    t = copy.deepcopy(tablero)
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j] == 0:
                t[i][j] = ""
    print("-" * ((7*len(t)+1)))
    for i in range(len(t)):
        for j in range(len(t)):
            print("| {:4}".format(t[i][j]), end=" ")
        print("|")
        print("-" * ((7*len(t)+1)))

def casillas_vacias(tablero):
    """ Devuelve una lista con las casillas vacias del tablero """
    vacias = []
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 0:
                vacias.append([i,j])
    return vacias

def rellenar_casillas(tablero, vacias):
    """ Devuelve tablero con casillas aleatorias rellena con 90% de 2 o 10% de 4 """
    n = random.choice([2,2,2,2,2,2,2,2,2,4])
    casilla = random.choice(vacias)
    tablero[casilla[0]][casilla[1]] = 1
    return tablero

#Programa principal
tablero = crear_tablero(4)
vacias = casillas_vacias(tablero)
tablero = rellenar_casillas(tablero,vacias)
movimientos = 1
mostrar_ganado = False

while True:
    os.system("cls")
    if movimientos != 0:
        vacias = casillas_vacias(tablero)
        tablero = rellenar_casillas(tablero,vacias)
    jugada = ""

    while jugada not in("a", "w", "s", "d"):
        os.system("cls")
        mostrar_tablero(tablero)
        jugada = input(" Mueve W-A-D-S -> ")
    else:
        if jugada == "d":
            tablero, movimientos = mover_derecha(tablero)
        elif jugada == "a":
            tablero, movimientos = mover_izquierda(tablero)
        elif jugada == "w":
            tablero, movimientos = mover_arriba(tablero)
        elif jugada == "s":
            tablero, movimientos = mover_abajo(tablero)
