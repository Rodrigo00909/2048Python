#ITERACION 1, esta mal planteado a futuro no ser boludo y revisar el juego antes de empezar.

#Juego 2048.
#Para llevar el mismo acabo se debe de partir en varias partes. Generar la matriz(tablero de juego)
#llenar el mismo con numeros al azar(dentro de los correspondientes de 2048)
#identificiar que posicion del tablero es la que el jugador va a desear mover
#Generar algun imput para los movimientos(wasd)
#contador de movimientos como posible highscore a guardar?
#identificar si gano
#identificar si perdio(no puede realizar mas movimientos)
from random import randint

matrizCuad = lambda orden, filler=0: [[filler]*orden for i in range(orden)]

def imprimir_matriz(matriz):
    #Imprime la matriz o tablero sobre el que se juega

    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%4d" %matriz[f][c], end=" ")
        print('\n')

def nueva_pantalla(n=50):
    #solucion momentanea? sin clear simplemente empujar las suficientes lineas?
    print('\n' * n)

def generar_recuadro():
    #genera los numeros de los recuadros en la grilla
    opciones = [2, 4]
    return opciones[randint(0, len(opciones) - 1)]

def iniciar_grilla(n=4):
    #genera la grilla o tablero de 4x4(se puede modificar en caso de ser necesario)
    orden = n
    matriz = matrizCuad(orden)
    
    for fil in range(orden):
        for col in range(orden):
            matriz[fil][col] = generar_recuadro()
    return matriz

def posicion_valida(pos, rango):
    #la funcion verifiva la posicion del recuadro dentro de la matriz
    #utilizar rango como la matriz dentro de la fila> mejor solucion?
    pos_valida = pos in range(len(rango))
    return pos_valida

def ingreso_posicion(matriz, tipo):
    #toma y valida fila o columna respecto a la posicion
    print(f'Ingrese la {tipo} del seleccionado: ', end='')
    pos = int(input())
    while not posicion_valida(pos, matriz):
        print(f'\n{tipo} invalida!! Intente de nuevo.')
        print(f'Ingrese la {tipo} del seleccionado: ', end='')
        pos = int(input())
    return pos

def ingreso_direccion():
    #obtiene y valida si la direccion del movimiento es valida

    movimientos = ['s', 'a', 'd', 'w']
    mov = input('Utilice (W,A,S,D) para ingresar la direccion a mover la grilla seleccionada: ')
    while mov not in movimientos:
        print('Movimiento invalido!! Intente de nuevo')
        mov = input('Ingrese la direccion a mover la grilla seleccionada: ')
    return mov

def ingreso_movimiento(matriz, fila, columna):
    #valida el movimiento que se realiza en la matriz
    
    movValido = False
    while not movValido:
        nuevaFila = fila
        nuevaCol = columna

        direccion = ingreso_direccion()
        if direccion == 's':
            nuevaFila += 1
        elif direccion == 'a':
            nuevaCol -= 1
        elif direccion == 'd':
            nuevaCol += 1
        else:
            nuevaFila -= 1
        movValido = posicion_valida(nuevaFila, matriz) and posicion_valida(nuevaCol, matriz[0])
        if not movValido:
            print('\nMovimiento no permitido! Intente nuevamente.\n')
    return nuevaFila, nuevaCol      

def mover_seleccion(matriz, fila, columna, nFila, nColumna):
    #efectuar el movimiento de la grilla seleccionada

    if matriz[nFila][nColumna] == matriz[fila][columna]:
        matriz[nFila][nColumna] *= 2

        matriz[fila][columna] = generar_recuadro()
        return 1
    else:
        return 0  

def hacer_jugada(matriz):
    #mueve una posicion a otra validando las coordenadas

    fila = ingreso_posicion(matriz, 'fila')
    columna = ingreso_posicion(matriz, 'columna')
    nFila, nCol = ingreso_movimiento(matriz, fila, columna)
    jug = mover_seleccion(matriz, fila, columna, nFila, nCol)
    return jug

def gano(matriz):
    #verifica si se alcanzo la condicion para ganar la partida
  

    ganado = False
    for fila in matriz:
        if 2048 in fila:
            ganado = True
    return ganado

def movimientos_disponibles(matriz):
    #verificar si aun quedan movimientos posibles en la grilla

    jugable = False
    fi = 0
    while fi < len(matriz) and not jugable:
        co = 0
        while co < len(matriz[0]) and not jugable:
            baldosa = matriz[fi][co]
            mov1, mov2, mov3, mov4 = False, False, False, False
            if fi > 0:
                mov1 = baldosa == matriz[fi - 1][co]
            if fi < len(matriz) - 1:
                mov2 = baldosa == matriz[fi + 1][co]
            if co > 0:
                mov3 = baldosa == matriz[fi][co - 1]
            if co < len(matriz) - 1:
                mov4 = baldosa == matriz[fi][co + 1]
            jugable = (mov1 or mov2 or mov3 or mov4)
            co += 1
        fi += 1
    return jugable

# programa principal
def __main__():
    print('\n\nJuego 2048\n\n\n')
    tablero = iniciar_grilla()
    ganado = False
    jugable = True
    movimientos = 0

    while not ganado and jugable:
        print(f'Movimientos: {movimientos}\n\n')
        print('Tablero:\n')
        imprimir_matriz(tablero)
        jugada = hacer_jugada(tablero)
        movimientos += jugada
        ganado = gano(tablero)
        jugable = movimientos_disponibles(tablero)
        nueva_pantalla()
    
    if ganado:
        print(f'En hora buena, ganaste! terminado el juego en {movimientos} jugadas!\n\n\n')
    else:
        print(f'El juego se atasco despues de {movimientos} movimientos GAME OVER')
    
    print('\n\nTablero final:')
    imprimir_matriz(tablero)

if __name__ == "__main__":
    __main__()