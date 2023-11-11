
def validarFila(fila):
        if len(fila) != 6: 
            print("La secuencia de ADN tiene que ser de 6 digitos")
            return False
        
        for i in fila:
            if i!="A"and i!="T" and i!="C" and i!="G":
                print("La secuencia de ADN no es valida, reviasa que sea una secuencia con A, T, C, G")
                return False
        return True
    


def vertical( adn, letra, i, j):
    return i + 3 < len(adn) and adn[i + 1][j] == letra and adn[i + 2][j] == letra and adn[i + 3][j] == letra

def horizontal(adn, letra, i, j):
    return j + 3 < 6 and adn[i][j + 1] == letra and adn[i][j + 2] == letra and adn[i][j + 3] == letra

def diagonal(adn, letra, i, j):
    return i + 3 < len(adn) and j + 3 < 6 and adn[i + 1][j + 1] == letra and adn[i + 2][j + 2] == letra and adn[i + 3][j + 3] == letra
def diagonalInversa(adn, letra,i,j):
    return i + 3 < len(adn) and j - 3 >= 0 and adn[i + 1][j -1] == letra and adn[i + 2][j - 2] == letra and adn[i + 3][j - 3] == letra

def is_mutant( adn):
    n = len(adn)
    contador = 0
    if n<=1:
        print("La secuencia contiene muy poca información: ") 
        return False
    for i in range(n):
        for j in range(6):
            letra = adn[i][j]
            
            
            if vertical(adn, letra, i, j) or horizontal(adn, letra, i, j) or diagonal(adn, letra, i, j) or diagonalInversa(adn, letra,i,j):
                contador += 1
            
            if contador > 1:
                return True
    
    
    return False
def condicionSalida(letraSalida):
    if letraSalida=="S":
        print("¡Continuemos con la busquedad!")
        return False
    else:
        print("Programa finalizado...")
        return True


print("-----------------------BUSCADOR DE MUTANTES-----------------------")
    
print("     Encontremos mutantes para poder luchar contra los X-Mens.")
print("--------------------------------------------------------------------")

salida = False
while not salida:
    
    dna = []
    cantidadFila =int(input("Ingrese la cantidad de filas de la secuencias del adn de la persona: "))

    for i in range(cantidadFila):
        condicion =False
        while not condicion:
            ADN=input(f"{i+1}) Ingrese la secuencia de ADN: (A, T, C, G): ").upper()
            condicion=validarFila(ADN)
        dna.append(ADN)
    print("Secuencia de ADN: ")
    contador=0
    for i in dna:
        contador+=1
        print(contador,") ",list(i))
    if is_mutant(dna):
        print("¡Felicitaciones, encontramos un mutante! ")
    else:
        print ("Este humano no es un mutante")
    
    letraSalida = input("""
        -------------------------------------------------
        ¿Desea volver a cargar otra secuencia?
        -------------------------------------------------
        -presione la letra S si desea buscar mas mutantes
        -presione cualquier letra para finalizar
        -------------------------------------------------
        Ingrese la letra: """).upper()
    salida= condicionSalida(letraSalida)
    



