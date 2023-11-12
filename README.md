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
## Casos: 
### Caso 1: 
Cargo la cantidad de fila recolectadas de secuencias de ADN del humano en este caso son 6.
Se ingresa las secuencias de ADN: 
- CATCAT
- GCTCAG
- CGTTAC
- CCTACG
- ACGGGC
- TTATAG
- El ADN ingresado NO corresponde a un mutante.
- por más que tenga una cadena vertical en la columna 3 con la misma letra (T), no corresponde porque necesita más de una cadena

### Caso 2:
Cargo la cantidad de fila recolectadas de secuencias de ADN del humano en este caso son 1.
Ingrese las secuencias de ADN: 
- CATCAT
- El ADN ingresado NO corresponde a un mutante.
- El programa identifica que al tener solo una secuencia la información es muy poca y lo cataloga como no mutante
### Caso 3
Cargo la cantidad de fila recolectadas de secuencias de ADN del humano en este caso son 7.
Ingreso las secuencias de ADN: 
- AAAACG
- TTTTAC
- CGTACG
- AAATCG
- TACGGC
- GCATGC
- CCCCCG
- El ADN ingresado corresponde a un mutante.
- Se encuentra en la fila 1 una secuencia de 4 "A", en la fila 2 una secuencia de 4 "T", en la fila "7" un secuencia de "C", y también se encuentra una diagonal
que comienza en la fila 2, columna 3  y finaliza en la fila 5 columna 2, por lo tanto a generado un contador de 4 secuencias de letras iguales superando el margen de dos,
es decir es Mutante.

### Caso 4
Cargo la cantidad de fila recolectadas de secuencias de ADN del humano en este caso son 5.
Ingreso las secuencias de ADN : 
- CATCAT
- ACGCAT
- CCCTAG
- CGTCAT
- TGATGA
- El ADN ingresado corresponde a un mutante.
- posee una cadena diagonal que comienza en la posicion fila 1, columna 1 y finaliza en la fila 5 columna 2 y otra cadena vertical en la columna 5, generando así
que cumpla con la condición de Mutante
