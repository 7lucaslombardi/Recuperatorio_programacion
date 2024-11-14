'''
1. Generar una función que calcule la media geométrica de filas o columnas de una matriz
cuadrada.
2. Generar una función que calcule la suma de las diagonales principal y secundaria de una
matriz.
Ejemplo:
1 2 3
4 5 6
7 8 9
Devuelve 30.
3. Generar una función que reciba una matriz y devuelva su transpuesta.
4. A la función del ejercicio 2 agregar un parámetro que permita seleccionar si lo que se
pretende recibir como retorno es la suma de ambas diagonales, solo la de la diagonal
principal o solo la de la diagonal secundaria.
'''

matriz = [[2, 6, 9],
        [7, 12, 15],
        [1, 5, 3]]

def calcular_media_geometrica(matriz: list, tipo : str) -> list:

    '''
    Calcula la media geometrica de una matriz
    Recibe una matriz y el tipo de calculo (filas o columnas)
    Devuelve una lista con las medias geometricas
    '''
    x = len(matriz)
    for fila in matriz:
        if len(fila) != x:
            print("La matriz no tiene la misma cantidad de filas y de columnas")

    lista = [0] * x

    if tipo == "fila":
        for i in range(x):
            producto = 1

            for numero in matriz[i]:
                producto *= numero
                lista[i] = producto ** (1 / x)

    elif tipo == "columna":
        for columna in range(x):
            producto = 1
            
            for fila in matriz:
                producto *= fila[columna]
                lista[columna] = producto ** (1 / x)

    return lista

media_geometrica = calcular_media_geometrica(matriz, "fila")
print(media_geometrica)

def sumar_diagonales(matriz: list, diagonal : str = "ambas") -> None:

    '''
    Suma las diagonales principales y secundarias de una matriz
    Recibe una matriz
    Devuelve None
    '''

    x = len(matriz)
    for fila in matriz:
        if len(fila) != x:
            print("La matriz no tiene la misma cantidad de filas y de columnas")

    suma_principal = 0
    suma_secundaria = 0

    for i in range(x):
        suma_principal += matriz[i][i]
        suma_secundaria += matriz[i][x - i - 1]

    if diagonal == "principal":
        print(f"La suma de la diagonal principal es {suma_principal}")
    elif diagonal == "secundaria":
        print(f"La suma de la diagonal secundaria es {suma_secundaria}")
    else:
        print(f"La suma de ambas diagonales es {suma_principal + suma_secundaria}")



sumar_diagonales(matriz, "principal")
sumar_diagonales(matriz, "secundaria")
sumar_diagonales(matriz, "ambas")

def devolver_transpuesta(matriz : list) -> list:

    x = len(matriz)
    for fila in matriz:
        if len(fila) != x:
            print("La matriz no tiene la misma cantidad de filas y de columnas")

    matriz_transpuesta = []
    
    for i in range(x):
        fila_transpuesta = []

        for j in range(x):

            fila_transpuesta.append(matriz[j][i])

        matriz_transpuesta.append(fila_transpuesta)

    return matriz_transpuesta

transpuesta = devolver_transpuesta(matriz)
print(transpuesta)

