import random 

def imprimirmatriz(matriz):
    """Imprime una matriz 4x4 del juego 2048"""
    filas = len(matriz)
    columnas = len(matriz[0])
    print("-"*21)
    for f in range(filas):
        for c in range(columnas):
            print("|%3d" %matriz[f][c], end=" ")
        print("|")
        print("-"*21)
    print()

# ESTAS DOS FUNCIONES HAY Q PULIRLAS SON UN ASCO
def primer_num_azar(matriz):
    """ Agrega un número a la matriz en un ratio de 90% para un 2 y un 10% para un 4 """
    while True:
        f = random.randint(0,3)
        c = random.randint(0,3)
        if mat[f][c] == 0:
            mat[f][c]= random.choice([2,2,2,2,2,2,2,2,2,4])
        break
    return mat

def segundo_num_azar(matriz):
    """ Agrega un segundo número a la matriz en un ratio de 90% para un 2 y un 10% para un 4 """
    while True:
        f = random.randint(0,3)
        c = random.randint(0,3)
        if mat[f][c] == 0:
            mat[f][c]= random.choice([2,2,2,2,2,2,2,2,2,4])
        break
    imprimirmatriz(mat)

#Programa Principal

mat = [[0]*4 for i in range (4)]
print()
primer_num_azar(mat)
segundo_num_azar(primer_num_azar)

