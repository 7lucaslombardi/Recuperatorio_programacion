def calcular_totales(matriz : list,  filas = True ) -> list:

    '''
    Calcula stock de camisetas a traves de un minimo
    Recibe una matriz y un booleano (si se calcula por filas o columnas)
    Devuelve el deposito o equipo que supere el stock minimo
    '''
    if filas:
        matriz_sumada = []

        for fila in matriz:
            suma = 0
            for elemento in fila:
                suma += elemento
            matriz_sumada += [suma]

    else:
        matriz_sumada = [0] * len(matriz[0])

        for i in range(len(matriz)):

            for j in range(len(matriz[0])):
                matriz_sumada[j] += matriz[i][j]

    return matriz_sumada


def estimar_stock(matriz_sumada: list, depositos: list, minimo: int) -> None:

        '''
        Calcula si el stock es mayor o menor que el minimo
        Recibe una dos listas y un minimo que es entero
        Devuelve None
        '''
        for i in range(len(matriz_sumada)):

            if matriz_sumada [i] > minimo:
                print(f"Hay mas de {minimo} en {depositos[i]}")

            else:
                print(f"No hay mas de {minimo} en {depositos[i]}")

def calcular_recaudacion(matriz : list, lista_precios : list 
                        = [100, 100, 100, 100, 100]) -> list:
    
    '''
    Calcula la recaudacion 
    Recibe una lista de cantidades y una lista de precios
    Devuelve una lista con la recaudacion
    '''
    
    lista_retorno = [0] * len(matriz)

    for i in range(len(matriz)):
        recaudacion = 0

        for j in range(len(matriz[i])):
            recaudacion += (matriz[i][j] * lista_precios[j])

        lista_retorno[i] = recaudacion

    return lista_retorno






