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

def buscoCeros(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] ==0:
                return True
    return False
        
    
#programa principal
    
filas = 4
columnas = 4
mat = [[0]*columnas for i in range (filas)]
#rellenarmatriz(mat)
imprimirmatriz(mat)

lleno= False

while lleno == False:
    if buscoCeros(mat):
        vacio=True
        while vacio:
            fila = random.randint(0,3)
            col = random.randint(0,3)
            if mat[fila][col] == 0:
                vacio = False
                opciones = [2, 4]
                mat[fila][col]= int(random.choice(opciones))
               
        imprimirmatriz(mat)
       
    else:
        lleno = True

print ("abajo")

for c in range(columnas):
        for f in range(filas -1):
            if mat[f][c] == mat[f+1][c] and mat[f][c] !=0:
                mat[f+1][c] *= 2
                mat[f][c] = 0

imprimirmatriz(mat)

print ("derecha")

for f in range(filas):
        for c in range(columnas -1):
            if mat[f][c] == mat[f][c+1] and mat[f][c] !=0:
                mat[f][c+1] *= 2
                mat[f][c] = 0

imprimirmatriz(mat)






    
