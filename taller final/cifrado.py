
def cifrado():
    
    table = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X'],
    ['Y', 'Z', 'A', 'B'],
    ['B', 'C', 'D', 'E']
    ]


    key = int(input("Ingrese clave para el cifrado: "))
    word = str(input("Ingrese palabra en mayuscula para cifrar: "))

    result = '' 
    for char in word:
        print(char)
        for i in range(len(table)):
            found = False
            for j in range(len(table[i])):
                if char == table[i][j]:
                    found = True
                    result += str(((i*i) + j) + key) 
                    
                    
                    break
    
            if found: break
    
    print(result)

cifrado()