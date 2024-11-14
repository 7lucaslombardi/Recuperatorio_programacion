def inicializar_matriz(cant_filas : int, cant_columnas : int, valor_inicial = 0) -> list:
    matriz = []
    
    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz

def cargar_aleatoriamente(matriz: list, fila : int, columna : int):
    
    continuar = "si"

    while continuar == "si":
        dato = int(input("Ingrese el numero a cargar: "))
        matriz[fila][columna] = dato
        continuar = input("Desea seguir cargando? (si o no): ")
