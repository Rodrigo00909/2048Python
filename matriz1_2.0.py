import random 

def imprimirmatriz(matriz):
    #autodetectamos el tamaño de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()
    print()

def rellenar_matriz(matriz):
    while True:
        f = random.randint(0,3)
        c = random.randint(0,3)
        if mat[f][c] == 0:
            mat[f][c]= random.choice([2,2,2,2,2,2,2,2,2,4])
        break
    return mat

def rellenar_matriz2(matriz):
    while True:
        f = random.randint(0,3)
        c = random.randint(0,3)
        if mat[f][c] == 0:
            mat[f][c]= random.choice([2,2,2,2,2,2,2,2,2,4])
        break
    imprimirmatriz(mat)
    return mat

#programa principal

mat = [[0]*4 for i in range (4)]
#rellenarmatriz(mat)
rellenar_matriz(mat)
rellenar_matriz2(rellenar_matriz)



        

""" chicos ese programa, genera una matriz de 4X4, iniciando con ceros las posiciones. Despues busca una posicion en la matriz y si esta con 0,
le asigna un numero, un 2 o 4. Lo hace hasta que la matriz no tenga mas cero
HAy que hacer una funcion con eso, y llamarlo después de cada jugada
hacer lo de las jugadas, para que sume y mueva, dependiendo si presiona w,d,a,s, """
