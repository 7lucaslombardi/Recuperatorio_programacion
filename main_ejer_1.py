'''
1. Obtener existencias: para ello deberá generar una función que cargue
secuencialmente, de tal forma que la intersección de cada fila y cada columna
corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
secuencial.
2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
3. Mostrar equipos que hay en stock más de 5.000 camisetas.
4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
encuentra.
5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
se deben restar los productos vendidos del stock y generar una matriz con la
recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.
'''
from funciones.auxiliares import *
from funciones.principales import *

depositos = ["tierra del fuego", "tucuman" , "mendoza", "bsas", "misiones", "santa fe"]
equipos = ["barcelona", "inter miami", "psg", "manchester city",  "real madrid"]
matriz_ejercicio = [[10, 15, 20, 25, 30], 
                    [5, 10, 15, 20, 25], 
                    [15, 20, 10000, 30, 35],
                    [20,50, 70, 90, 120], 
                    [300, 500, 200, 700, 1000], 
                    [2000, 100, 600, 40, 700]]

ejecutar = True

while ejecutar == True:

    print("Seleccione una opcion:")
    print("1- Obtener existencias")
    print("2- Mostrar depositos con mas de 10000 camisetas")
    print("3- Mostrar equipos con mas de 5000 camisetas")
    print("4- Mostrar maxima cantidad de camisetas por equipo")
    print("5- Cargar ventas")
    print("6- Salir ")
    
    opcion = input("Ingrese la opcion a realizar: ")

    match opcion:
        case "1":
            matriz_ejercicio = inicializar_matriz(len(depositos), len(equipos), 0)
            print(matriz_ejercicio)

            for i in range(len(depositos)):
                for j in range(len(equipos)):

                    cantidad = int(input(f"Ingrese cantidad de camisetas de {equipos[j]} en {depositos[i]}: "))
                    matriz_ejercicio[i][j] = cantidad
            print(matriz_ejercicio)
        
        case "2":
            matriz_filas = calcular_totales(matriz_ejercicio, True)
            print(f"Suma por filas: {matriz_filas}")

            estimar_stock(matriz_filas, depositos, 10000)

        case "3":
            matriz_columnas = calcular_totales(matriz_ejercicio, False)
            print(f"Suma por columnas: {matriz_columnas}")
            
            estimar_stock(matriz_columnas, equipos, 5000)

        case "4":

            for i in range(len(equipos)):
                bandera = True

                for j in range(len(depositos)):
                    if bandera == True:
                        maximo = matriz_ejercicio[j][i]
                        deposito = depositos[j]
                        bandera = False

                    elif matriz_ejercicio[j][i] > maximo:
                        maximo = matriz_ejercicio[j][i]
                        deposito = depositos[j]

                print(f"El deposito con mas camisetas de {equipos[i]} es {deposito}")

        case "5":
            matriz_recaudacion = calcular_recaudacion(matriz_ejercicio)
            print(f"Matriz recaudacion: {matriz_recaudacion}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        case "6":
            print("Se salio del ejercicio")
            ejecutar = False