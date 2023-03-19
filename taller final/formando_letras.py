def formando_L():

    for i in range(filas):
        for j in range(columnas):
            if 0 <= i <= 5 and j == 1:
                print(caracter, end="")
            elif i == 6 and 1 <= j <= 5:
                print(caracter, end="")
            else:
                print(' ', end="")
        print()



def formando_M():
    for i in range(filas):
        for j in range(columnas):
            if (i == 0 or i == 1 or 4 <= i <= 6) and (j == 1 or j == 11):
                print(caracter, end='')
            elif i == 2 and (j == 1 or j == 3 or j == 9 or j == 11):
                print(caracter, end='')
            elif i == 3 and (j == 1 or j == 6 or j == 11):
                print(caracter, end='')
            else:
                print(' ', end='')
        print()

print("        Bienvenido  " )
print("#Nota: Para formar la letra M las columnas tienen que ser mayor 12!!")


letra = str(input("Ingrese letra a formar entre la 'L' y la 'M': "))
while letra != 'L' and letra != 'M':
   letra = str(input("Ingrese letra valida entre la 'L' y la 'M': "))


if letra == 'L':
    columnas = int(input("Ingrese numero de columnas: "))
    filas = int(input("ingrese numero de filas: "))
    caracter = input("Ingrese caracter con que quiere llenar la letra: ")
    print(formando_L())
if letra == 'M':
    columnas = int(input("Ingrese numero de columnas: "))
    filas = int(input("ingrese numero de filas: "))
    while columnas < 12:
        columnas = int(input("Ingrese numero de columnas valido: "))
    caracter = input("Ingrese caracter con que quiere llenar la letra: ")
    print(formando_M())