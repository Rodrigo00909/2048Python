import random
"""
Chicos, para iniciar el juego y completar la matriz de juego, deberíamos usar un random.sample. o shuffler. 
Ya que cuando inicia todos los valores de matriz tienen que ser ceros, salvo dos, que pueden ser 2 o 4
Y despues si, tirar un random que sea 2 o 4
Ya se está inicializando con ceros las matriz, lo que habría que hacer, es buscar dos posiciones al azar de la matriz,
fila y columnas y una vez que elige al azar la fila o columna, hacer otro random poniéndole un 2 o 4, siempre y cuando 
esa posicion sea un cero, de no ser así que elija otra posicion de la matriz hasta encontrar un cero
"""


def comenzar_juego():
    #cambiar por lambda asi cubrimos mas temas
    matriz=[]
    for i in range(4):
        matriz.append([0]*4)
    
    print('Para jugar recuerde utilizar las teclas WASD: w=arriba, s=abajo, a=izquierda y d= derecha')
    
    agregar_nuevo_num(matriz)
    return matriz


# VOLVER A VER CICLO INFINITO
## debe agregar 2 valores 2 en posiciones al azar vacias despues de cada movimiento
'''
funcion para agregar numero 2 en la grilla despues de cada movimiento

'''
def agregar_nuevo_num(matriz):
    '''
    elige primero la fila y la columna al azar
'''
    f = random.randint(0,3)
    c = random.randint(0,3)
    
    while (matriz[f] != 0):
        '''
        el loop debe de romper cuando este vacia la celda
'''
        f = (random.randint(0,3))
        c = (random.randint(0,3))
        '''
        agrega el valor 2
'''
    matriz[f]=2
# CICLO INFINITO AGREGAR NUEVO NUM

def estado_actual(matriz):
    for f in range(4):
        for c in range(4):
            if(matriz[f][c] == 2048):
                return 'GANASTE CAMPEON!'
    
    for f in range(4):
        for c in range(4):
            if(matriz[f][c] == 0):
                return 'aun no ganaste'
    
    for f in range(3):
        for c in range(3):
            if(matriz[f][c] == matriz[f+1][c] or matriz[f][c] == matriz[f][c+1]):
                return 'aun no ganaste'
   
    for f in range(3):
        for c in range(3):
            if(matriz[3][c] == matriz[3][c+1]):
                return 'aun no ganaste'
            
    for f in range(3):
        for c in range(3):
            if(matriz[f][3] == matriz[f+3][c]):
                return 'aun no ganaste'
    return 'GAME OVER... '


def comprimir(matriz):
    cambio = False
    nueva_matriz=[]
    for i in range(4):
        nueva_matriz.append([0]*4)
    for f in range(4):
        posicion = 0
        
        for c in range(4):
            if(matriz[f][c] != 0):
                nueva_matriz[f][posicion] = matriz[f][c]
                if(c!=posicion):
                    cambio=True
                posicion+=1
    return nueva_matriz, cambio

def combinar(matriz):
    cambio = False
    for f in range(4):
        for c in range(3):
            if(matriz[f][c] == matriz[f][c+1] and matriz[f][c] != 0):
                matriz[f][c] = matriz[f][c]*2
                matriz[f][c+1]=0
                
                cambio = True
    return matriz, cambio

def reves(matriz):
    nueva_matriz=[]
    for f in range(4):
        nueva_matriz([])
        for c in range(4):
            nueva_matriz[f].append(matriz[f][3-f])
    return nueva_matriz

def transponer(matriz):
    nueva_matriz =[]
    for f in range(4):
        nueva_matriz.append([])
        for c in range(4):
            nueva_matriz[f].append(matriz[c][f])
    return nueva_matriz

def mover_izquierda(grilla):
    nueva_grilla, cambio1 = comprimir(grilla)
    nueva_grilla, cambio2 = combinar(grilla)
    cambio = cambio1 or cambio2
    nueva_grilla, temporal = comprimir(grilla)
    
    return nueva_grilla, cambio

def mover_derecha(grilla):
    nueva_grilla = reves(grilla)
    nueva_grilla, cambio = mover_izquierda(nueva_grilla)
    nueva_grilla = reves(nueva_grilla)
    
    return nueva_grilla, cambio

def mover_arriba(grilla):
    nueva_grilla=transponer(grilla)
    nueva_grilla, cambio = mover_izquierda(nueva_grilla)
    nueva_grilla =transponer(nueva_grilla)
    
    return nueva_grilla, cambio

def mover_abajo(grilla):
    nueva_grilla= transponer(grilla)
    nueva_grilla, cambio = mover_derecha(nueva_grilla)
    nueva_grilla = transponer(nueva_grilla)
    
    return nueva_grilla, cambio
    


# PROGRAMA PRINCIPALLLLLLL

matriz= comenzar_juego()
#cuenta como excep, queda mejor con try
while(True):
    x= input('Ingrese un comando')
    
    if(x=='w'):
        matriz,temp = mover_arriba(matriz)
        estado= estado_actual(matriz)
        print(estado)
        if(estado == 'aun no ganaste'):
            agregar_nuevo_num(matriz)
        else:
            break
    elif(x=='s'):
        matriz, temp = mover_abajo(matriz)
        estado = estado_actual(matriz)
        print(estado)
        if(estado == 'aun no ganaste'):
            agregar_nuevo_num(matriz)
        else:
            break
    elif(x=='a'):
        matriz, temp = mover_izquierda(matriz)
        estado = estado_actual(matriz)
        print(estado)
        if(estado == 'aun no ganaste'):
            agregar_nuevo_num(matriz)
        else:
            break
    elif(x=='d'):
        matriz, temp = mover_abajo(matriz)
        estado = estado_actual(matriz)
        print(estado)
        if(estado == 'aun no ganaste'):
            agregar_nuevo_num(matriz)
        else:
            break
    else:
        print('La tecla que ingresaste no es valida')
    print(matriz)
    #agregar movimiento con counter(usarlo para el high score)
