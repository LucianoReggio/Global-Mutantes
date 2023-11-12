# Global-Mutantes
## Alumno: Luciano-Reggio
## Legajo institucional: 51629
## Descripción del código:
El código proporciona un programa interactivo para buscar mutantes a través de secuencias de ADN. La detección de mutantes se realiza verificando si hay cuatro letras idénticas (A, T, C, o G) en un secuencia de 6 letras en una cantidad de filas introduciada por el usuario consecutivas en forma vertical, horizontal, diagonal o diagonal inversa en una matriz de ADN.

## Funciones:
validarFila(fila): Valida si la fila de ADN proporcionada cumple con las condiciones establecidas. Verifica la longitud de la fila y si solo contiene las letras A, T, C, o G.

vertical(adn, letra, i, j): Comprueba si hay cuatro letras idénticas en forma vertical a partir de la posición (i, j) en la matriz de ADN.

horizontal(adn, letra, i, j): Comprueba si hay cuatro letras idénticas en forma horizontal a partir de la posición (i, j) en la matriz de ADN.

diagonal(adn, letra, i, j): Comprueba si hay cuatro letras idénticas en forma diagonal a partir de la posición (i, j) en la matriz de ADN.

diagonalInversa(adn, letra, i, j): Comprueba si hay cuatro letras idénticas en forma diagonal inversa a partir de la posición (i, j) en la matriz de ADN.

is_mutant(adn): Verifique si la matriz de ADN contiene al menos dos secuencias de cuatro letras idénticas en alguna dirección (vertical, horizontal, diagonal o diagonal inversa). Devuelve Truesi es un mutante y Falseen caso contrario.

condicionSalida(letraSalida): Verifica la letra de salida proporcionada por el usuario. Si es "S", el programa comenzará buscando mutantes; De lo contrario, el programa se cerrará.



## Instrucciones de ejecución:
Siga las instrucciones proporcionadas por el programa para ingresar la cantidad de filas y las secuencias de ADN.
Evalúe los resultados y decida si cargar otra secuencia o finalizar el programa.
