import random 
from pprint import pprint
matriz = []


def imprimirmatriz():
    i= 0
    m= int(input("Digite una dimension Filas: "))
    n= int(input("Digite una dimension Columnas: "))
    while m < 0 : 
        m= int(input("Digite una dimension Filas valido: "))    
    while n < 0 :
        n= int(input("Digite una dimension Columnas valido: "))
    for i in range(0,m):
        for j in range(0,n):
            numerosA= random.randint(100,300)
            print(numerosA," ", end='')
        print(" ")



def imprimirbordes():   
    m= int(input("Digite una dimension Filas: "))
    n= int(input("Digite una dimension Columnas: "))
    while m < 0 : 
        m= int(input("Digite una dimension Filas valido: "))    
    while n < 0 :
        n= int(input("Digite una dimension Columnas valido: "))
    for i in range(0,n):
        numerosA= random.randint(100,300)
        print (numerosA," ", end='')
    print()
    for i in range(0,m-2):
        numerosA= random.randint(100,300)
        print(numerosA," ", end='')
        for j in range(0,n-2):
            print("     ", end='')
        print(numerosA," ")
    for i in range(0,n):
        numerosA= random.randint(100,300)
        print(numerosA," ", end='')
    
def imprimirdiagonal():
    
    i=0
    j=0

    m=int(input("ingrese un lado: "))
    n=int(input("ingrese un lado: "))
    while m % 2 == 0 :
        m=int(input("ingrese un lado numero valido impar: "))
    while n % 2 == 0 :
        n=int(input("ingrese un lado numero valido impar: "))
    for i in range(0,m):
        for j in range(0,n):
            if i==j or i+j==n-1:
                numerosA= random.randint(100,300)
                print(numerosA," ", end="")
            else:
                print("     ", end="")
        
        print(" ")


def imprimircruz():   
    filas=int(input("ingrese un lado: "))
    columnas=int(input("ingrese un lado: "))

    while filas % 2 == 0:
        filas=int(input("ingrese un lado valido impar: "))
        
    while columnas < 0:
        columnas=int(input("ingrese columnas valido impar: "))

    for i in range(filas):
        for j in range(columnas):
            if i == 2 :
                numerosA= str(random.randint(100,300))
                
                print(f"{numerosA} ", end='')
            elif j == columnas-1:
                numerosA= str(random.randint(100,300))
                print(" "*columnas," "*(columnas-4),numerosA, end='')

        print("", end='')
            

        print(" ")


    print()



def menu():
    print("   \n            MENU \n ")
    print(" 1. Imprimir matriz  \n")
    print(" 2. Imprimir bordes \n")
    print(" 3. Imprimir diagonales \n")
    print(" 4. Imprimir cruz \n")
    print(" 0. salir \n")
    opcion = int(input("Ingrese opcion:"))
    while (opcion < 0 or opcion > 4):
        opcion = int(input("Ingrese opcion valida: "))
    return opcion

op = menu
while op != 0:
    if op == 1:
        imprimirmatriz()
    else: 
        if op == 2: 
            imprimirbordes()
        else:
            if op == 3:
                imprimirdiagonal()
            else:
                if op == 4:
                    imprimircruz()
                else:
                    if op == 0: 
                        print("Hasta luego, termino el programa")
    op = menu()
