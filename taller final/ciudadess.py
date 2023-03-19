from random import uniform

ciudades = int(input("Ingrese numero de ciudades: "))
matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]

def mayor_precipitacion(matriz):
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]
    for f in matriz:
        print(f)

    for i in range(len(matriz[0]))  :  
        mayor=0  
        for j in range(len(matriz)) :
        
            if matriz[j][i] >= mayor:
                mayor = matriz[j][i]
                k= j        
        print("En la ciudad:",i+1 , "en el dia:",k+1, "se presento una mayor precipitacion de:",mayor )




def promedio_ciudad(matriz):
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]
    for f in matriz:
        print(f)

    for i in range(len(matriz[0])):

        suma = 0.0
        for j in range(len(matriz)):
            suma = suma + matriz[j][i]

        promedio = suma/(j+1)

        print("El promedio de la ciudad:",i+1, "es igual a:", promedio.__round__(1))




def promedio_general(matriz):
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]
    for f in matriz:
        print(f)
    k = ciudades*30
    suma = 0
    for i in range(len(matriz[0])):
        
        for j in range(len(matriz)):
            suma = suma + matriz[j][i]

    print(suma)  
    promedio = suma/(k)
    print(promedio)
    p = 0
    for i in range(len(matriz[0])):
        mayor = 0
        for j in range(len(matriz)):
            suma = suma + matriz[j][i]
            if matriz[j][i] >= promedio:
                mayor = matriz[j][i]
                p = j+1     
                print("En la ciudad",i+1 ,  "con una precipitacion de:",mayor, " y el dia es",p )


def menor_precipitacion(matriz):
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]
    for f in matriz:
        print(f)
        
    k= 0    
    for i in range(len(matriz[0]))  :  
        menor=6  
        for j in range(len(matriz[i])) :
        
            if matriz[i][j] <= menor:
                menor = matriz[i][j]
                k = j+1
        print("El dia", k , "en la ciudad", i+1, "con menor precipitacion fue:", menor )           


def menu():
    print("   \n            MENU \n ")
    print(" 1. Dia de mayor precipitacion de cada ciudad  \n")
    print(" 2. Precipitacion promedio de cada ciudad \n")
    print(" 3. Determinacion de dias en cuales fue mayor la precipitacion al promedio \n")
    print(" 4. Ciudad de menos precipitacion de cada dia \n")
    print(" 0. salir \n")
    opcion = int(input("Ingrese opcion:"))
    while (opcion < 0 or opcion > 4):
        opcion = int(input("Ingrese opcion valida: "))
    return opcion

op = menu
while op != 0:
    if op == 1:
        print(mayor_precipitacion(matriz))
    else: 
        if op == 2: 
            promedio_ciudad(matriz)
        else:
            if op == 3:
                promedio_general(matriz)
            else:
                if op == 4:
                    menor_precipitacion(matriz)
                else:
                    if op == 0: 
                        print("Hasta luego, termino el programa")
    op = menu()
