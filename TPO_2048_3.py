import random
import copy

def crear_matriz(mat):
    """ Crea una matriz de 4x4"""
    matriz = []
    for i in range(mat):
        matriz.append([])
        for j in range(mat):
            matriz[i].append(0)
    return matriz

def mostrar_matriz(matriz):
    """ Crea una copia de la matriz recibida y reemplaza los 0 por espacios vacios """
    m = copy.deepcopy(matriz)
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 0:
                m[i][j] = ""
    print("-" * ((7*len(m)+1)))
    for i in range(len(m)):
        for j in range(len(m)):
            print("| {:4}".format(m[i][j]), end=" ")
        print("|")
        print("-" * ((7*len(m)+1)))

def vaciar_matriz(matriz):
    """ Devuelve una lista con la matriz vacia """
    matrizVacia = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                matrizVacia.append([i,j])
    return matrizVacia

def rellenar_matriz(matriz, matrizVacia):
    """ Devuelve matriz con casillas aleatorias rellena con 90% de 2 o 10% de 4 """
    n = random.choice([2,2,2,2,2,2,2,2,2,4])
    casilla = random.choice(matrizVacia)
    matriz[casilla[0]][casilla[1]] = n
    return matriz

def derecha(m):
    """ Mueve los indices a la derecha y realiza la suma""" 
    mov = 0
    for y in range(len(m)):
        mezclas = []
        for i in range(len(m)-1):
            for x in range(-2,-len(m)-1,-1):
                if m[y][x] != 0 and m[y][x+1] == 0:
                    m[y][x+1] = m[y][x]
                    m[y][x] = 0
                    mov+=1
                elif m[y][x] != 0 and m[y][x] == m[y][x+1] and x not in mezclas and x-1 not in mezclas:
                    m[y][x+1] = m[y][x+1] * 2
                    m[y][x] = 0
                    mezclas.append(x)
                    mov+=1
    return m, mov

def izquierda(m):
    """ Mueve los indices a la izquierda y realiza la suma""" 
    mov = 0
    for y in range(len(m)):
        mezclas = []
        for i in range(len(m)-1):
            for x in range(1,len(m)):
                if m[y][x] != 0 and m[y][x-1] == 0:
                    m[y][x-1] = m[y][x]
                    m[y][x] = 0
                    mov+=1
                elif m[y][x] != 0 and m[y][x] == m[y][x-1] and x not in mezclas and x+1 not in mezclas:
                    m[y][x-1] = m[y][x-1] * 2
                    m[y][x] = 0
                    mezclas.append(x)
                    mov+=1
    return m, mov

def abajo(m):
    """ Mueve los indices abajo y realiza la suma""" 
    mov = 0
    for x in range(len(m)):
        mezclas = []
        for i in range(len(m)-1):
            for y in range(-2,-len(m)-1,-1):
                if m[y][x] != 0 and m[y+1][x] == 0:
                    m[y+1][x] = m[y][x]
                    m[y][x] = 0
                    mov+=1
                elif m[y][x] != 0 and m[y][x] == m[y+1][x] and y not in mezclas and y-1 not in mezclas:
                    m[y+1][x] = m[y+1][x] * 2
                    m[y][x] = 0
                    mezclas.append(y)
                    mov+=1
    return m, mov

def arriba(m):
    """ Mueve los indices arriba y realiza la suma""" 
    mov = 0
    for x in range(len(m)):
        mezclas = []
        for i in range(len(m)-1):
            for y in range(1,len(m)):
                if m[y][x] != 0 and m[y-1][x] == 0:
                    m[y-1][x] = m[y][x]
                    m[y][x] = 0
                    mov+=1
                elif m[y][x] != 0 and m[y][x] == m[y-1][x] and y not in mezclas and y+1 not in mezclas:
                    m[y-1][x] = m[y-1][x] * 2
                    m[y][x] = 0
                    mezclas.append(y)
                    mov+=1
    return m, mov

def gano_juego(matriz):
    """ Devuelve True si se alcanza 2048 """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 2048:
                return True
    return False

def perdio_juego(matriz):
    """ Recorre el matriz y comprueba si no hay mas movimientos """
    # Comprobar si no hay dos casillas contiguas con el mismo valor
    final = True
    for y in range(len(matriz)):
        for x in range(len(matriz)-1):
            if matriz[y][x] == matriz[y][x+1]:
                final = False
    
    for y in range(len(matriz)-1):
        for x in range(len(matriz)):
            if matriz[y][x] == matriz[y+1][x]:
                final = False

    return final

#Programa principal
matriz = crear_matriz(4)
matrizVacia = vaciar_matriz(matriz)
matriz = rellenar_matriz(matriz,matrizVacia)
movimientos = 1
mov_der = 0
mov_iz = 0
mov_arriba = 0
mov_abajo = 0
mov_total = 0
mostrar_ganado = False
print()
print("------------ JUEGO 2048 ------------")
print()

while True:
    if movimientos != 0:
        matrizVacia = vaciar_matriz(matriz)
        matriz = rellenar_matriz(matriz,matrizVacia)
    jugada = ""

    while jugada not in("a", "w", "s", "d"):
        mostrar_matriz(matriz)
        print(" Asegurate de tener BLOQ MAYUS DESACTIVADO")
        jugada = input(" Juega con las teclas:\n W = ARRIBA \n S = ABAJO \n D = DERECHA \n A = IZQUIERDA: \n ")
    else:
        if jugada == "d":
            mov_der += 1
            matriz, movimientos = derecha(matriz)
        elif jugada == "a":
            mov_iz += 1
            matriz, movimientos = izquierda(matriz)
        elif jugada == "w":
            mov_arriba += 1
            matriz, movimientos = arriba(matriz)
        elif jugada == "s":
            mov_abajo += 1
            matriz, movimientos = abajo(matriz)
    

    mov_total = mov_der+mov_iz+mov_arriba+mov_abajo
    # Si gano_juego es verdadero y mostrar gano_juego es falso entonces:
    if gano_juego(matriz) and not mostrar_ganado:
        mostrar_ganado = True
        mostrar_matriz(matriz)
        print("------- ¡FELICITACIONES! ¡GANASTE! --------")
        print("Movimientos totales: ",mov_total)
        op = input("Querés jugar denuevo? (s) o (n)")
        if op != "s":
            break

    if len(vaciar_matriz(matriz)) == 0 and perdio_juego(matriz) == True:
        print("------- PERDISTE :( --------")
        print("----------------------------")
        break