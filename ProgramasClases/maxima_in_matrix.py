import random

'''
2) Este ejercicio es para practicar recorridos sobre una lista de listas (matriz) en el contexto del curso.
SPEC: Sea a una lista de listas como se usó en es_simetrica.  Le decimos una matriz.
Escriba maxima_in_matrix(a list[list[int]]) -> list[list[int]]  que retorna todos los índices [i, j] tales que a[i][j] es el elemento máximo de los valores en a. Se retorna una lista de listas [i,j]. Use buen estilo y haga un caso de prueba para n=5, que tenga el máximo en 3 distintas posiciones de a (en una esquina, en el centro y otro lugar fuera de la diagonal que no sea una esquina). Hago otra caso donde el máximo está sólo en el centro.

b) Haga el análisis 6 pasos de  maxima_in_matrix  (Operación de interés es sólo [],  acceso a lista). Para el paso 6,  debe ingeniárselas para generar matrices aleatorias que vayan creciendo en tamaño. Consulte el módulo de python random si es necesario.
'''
def maxima_in_matrix(a:'list[list[int]]')->'list[list[int]]':
    max_list = []
    max_num = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            test = a[i][j]
            if test > max_num:
                max_list = []
                max_num = test
                max_list.append([i,j])
            elif test == max_num:
                max_list.append([i,j])
    return max_list

a_1 = [[5,4,3,2,1], [4,3,2,1,0], [2,1,5,4,3], [3,5,1,2,4], [0,1,2,3,4]]
a_2 = [[1,4,3,2,5], [4,3,2,1,0], [2,1,5,4,3], [3,1,5,2,4], [0,1,2,3,4]]
a_3 = [[1,4,3,2,0], [4,3,2,1,0], [2,1,5,4,3], [3,1,5,2,4], [5,1,2,3,4]]
a_4 = [[1,4,3,2,0], [4,3,2,1,0], [2,1,5,4,3], [3,1,5,2,4], [0,1,2,3,5]]
a_5 = [[1,4,3,2,0], [4,3,2,1,0], [2,1,5,4,3], [3,1,0,2,4], [0,1,2,3,4]]

print(maxima_in_matrix(a_1))
print(maxima_in_matrix(a_2))
print(maxima_in_matrix(a_3))
print(maxima_in_matrix(a_4))
print(maxima_in_matrix(a_5))

'''
Analisis 6 pasos:
1) Tamaño datos (n)
    n = len(a) * len(a[0])
    
2) Operaciones de interes
Las operaciones de interes son:
=

>
[] // esta es la unica que me pidieron contar, pero contemos el resto para ver
==
range() 
append() // append no es constante entonces no se va a contar
Todos cuentan como 1

3) Ecuación del tiempo de corrida T_simetrica(n)

T_maxima(0) =   0 (caso n = 0)
Dividir por partes:
# Parte 1
max_list = []
max_num = 0

# Parte 2.1
for i in range(len(a)):
    # Parte 2.2
    for j in range(len(a[i])):
        test = a[i][j]
        if test > max_num:
            max_list = []
            max_num = test
            max_list.append([i,j])
        elif test == max_num:
            max_list.append([i,j])
return max_list

T_maxima(n) =   5(n - 1) + T_simetrica(n - 1) (caso n > 0)

4) Resolver la ecuación
Si n > 0
T_simetrica(n) =   5(n - 1) + T_simetrica(n - 1)
               =   5(n - 1) + 5(n - 2) + T_simetrica(n - 2)
               =   5(n - 1) + 5(n - 2) + 5(n - 3) + ... + 5(2) + 5(1)
               =   5((n - 1) + (n - 2) + (n - 3) + ... + (2) + (1))
               =   5 (( n - 1)n)/2    (es una suma de Gauss)
T_simetrica(n) = 5 (( n - 1)n)/2

5) Clasificar el orden de T_simetrica(n)
Tenemos:
5 (( n - 1)n)/2 = 5( n**2/2 - n/2 ) = 5/2( n**2) - 5/2(n) ) ~ O(n**2)
Por lo tanto T_simetrica es O(n**2)

6) Generar datos empíricos
'''

def maxima_in_matrix_instrumentado(a:'list[list[int]]')->'list[list[int]]':
    contador_operaciones = 0
    max_list = []
    max_num = 0
    contador_operaciones += 3 # dos ='s y un range()
    for i in range(len(a)):
        contador_operaciones += 1 # el range()
        for j in range(len(a[i])):
            test = a[i][j]
            contador_operaciones += 3
            if test > max_num:
                contador_operaciones += 1 # el >
                max_list = []
                max_num = test
                max_list.append([i,j])
                contador_operaciones += 3 # los 2 ='s y el append()
            elif test == max_num:
                contador_operaciones += 2 # el > y el ==
                max_list.append([i,j])
                contador_operaciones += 1 # el append()
            contador_operaciones += 2 # > y ==
    return contador_operaciones

def test_maxima_in_matrix_instrumentado(filename, init, maxi, inc):
    file = open(filename, 'W')
    file.write('n;time\n')
    for n in range(init, maxi, inc):
        a = list(range(n))
        for i in range(n):
            a[i] = list(range(n))
    file.close()
    return 0