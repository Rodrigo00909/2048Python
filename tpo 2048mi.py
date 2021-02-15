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
    tablero[casilla[0]][casilla[1]] = 2
    return tablero

def mover_derecha(t):
    """ Mueve las casillas a la derecha y realiza la suma""" 
    mov = 0
    for y in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for x in range(-2,-len(t)-1,-1):
                if t[y][x] != 0 and t[y][x+1] == 0:
                    t[y][x+1] = t[y][x]
                    t[y][x] = 0
                    mov+=1
                elif t[y][x] != 0 and t[y][x] == t[y][x+1] and x not in mezclas and x-1 not in mezclas:
                    t[y][x+1] *= 2
                    t[y][x] = 0
                    mezclas.append(x)
                    mov+=1
    return t, mov

def mover_izquierda(t):
    """ Mueve las casillas a la izquierda y realiza la suma""" 
    mov = 0
    for y in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for x in range(1,len(t)):
                if t[y][x] != 0 and t[y][x-1] == 0:
                    t[y][x-1] = t[y][x]
                    t[y][x] = 0
                    mov+=1
                elif t[y][x] != 0 and t[y][x] == t[y][x-1] and x not in mezclas and x+1 not in mezclas:
                    t[y][x-1] *= 2
                    t[y][x] = 0
                    mezclas.append(x)
                    mov+=1
    return t, mov

def mover_abajo(t):
    """ Mueve las casillas abajo y realiza la suma""" 
    mov = 0
    for x in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for y in range(-2,-len(t)-1,-1):
                if t[y][x] != 0 and t[y+1][x] == 0:
                    t[y+1][x] = t[y][x]
                    t[y][x] = 0
                    mov+=1
                elif t[y][x] != 0 and t[y][x] == t[y+1][x] and y not in mezclas and y-1 not in mezclas:
                    t[y+1][x] *= 2
                    t[y][x] = 0
                    mezclas.append(y)
                    mov+=1
    return t, mov

def mover_arriba(t):
    """ Mueve las casillas arriba y realiza la suma""" 
    mov = 0
    for x in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for y in range(1,len(t)):
                if t[y][x] != 0 and t[y-1][x] == 0:
                    t[y-1][x] = t[y][x]
                    t[y][x] = 0
                    mov+=1
                elif t[y][x] != 0 and t[y][x] == t[y-1][x] and y not in mezclas and y+1 not in mezclas:
                    t[y-1][x] *= 2
                    t[y][x] = 0
                    mezclas.append(y)
                    mov+=1
    return t, mov

def ganador(tablero):
    """ Devuelve True si se alcanza 2048 """
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 2048:
                return True
    return False

def sin_movimientos(tablero):
    """ Recorre el tablero y comprueba si no hay mas movimientos """
    # Comprobar si no hay dos casillas contiguas con el mismo valor
    final = True
    for y in range(len(tablero)):
        for x in range(len(tablero)-1):
            if tablero[y][x] == tablero[y][x+1]:
                final = False
    
    for y in range(len(tablero)-1):
        for x in range(len(tablero)):
            if tablero[y][x] == tablero[y+1][x]:
                final = False

    return final

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
    
    # Si ganador es verdadero y mostrar ganador es falso entonces:
    if ganador(tablero) and not mostrar_ganado:
        mostrar_ganado = True
        os.System("cls")
        mostrar_tablero(tablero)
        print("------- GANASTE --------")
        op = input("Quieres Continuar? (s)")
        if op != "s":
            break

    if len(casillas_vacias(tablero)) == 0 and sin_movimientos(tablero) == True:
        print("------- PERDISTE --------")
        print("-------------------------")
        break

