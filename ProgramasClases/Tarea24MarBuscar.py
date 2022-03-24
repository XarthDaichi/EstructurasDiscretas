'''
Analisis 6-pasos de buscar_while
PASO-1: Tamano de datos (n)
El tamano esta dado por la cantidad de elementos en a
n = len(a)

PASO-2: Operaciones de Interes
Candidatos
T=  es una constante a (constante dependiente de la infraestructura)
T<  es una constante b
==  es una constante c
[]  es una constante d
+=  es una constante e
len es una constante f
Peor caso: todas son iguales a la mas grande de todas, como supuesto
Asumimos que vale 1 (unidad de tiempo), según el más alto

PASO-3

PASO-4

PASO-5

PASO-6

'''
def buscar_while_instrumentado(x:int, a:'list[int]')-> int:
    contador_operaciones = 0
    p:int = 0
    contador_operaciones += 1
    no_salir = p < len(a)
    contador_operaciones += 2
    while no_salir:
        if x == a[p]:
            contador_operaciones += 2
            return contador_operaciones
        else:
            contador_operaciones += 2
            p += 1
            contador_operaciones += 1
        no_salir = p < len(a)
        contador_operaciones += 2
    return contador_operaciones

'''
Analisis de 6 pasos de buscar_for
PASO-1 Tamano de datos (n)
El tamano es determinado por la cantidad de elementos de la lista
n = len(a)

PASO-2


PASO-3
PASO-4
PASO-5
PASO-6
'''

def buscar_for_instrumentado(x:int, a:'list[int]') -> int:
    contador_operaciones = 0
    contador_operaciones += 1 #crear range y todas las operaciones dentre de este
    for p in range(len(a)):
        contador_operaciones += 2 # == y []
        if x == a[p]:
            return contador_operaciones
    return contador_operaciones

def test_buscar_instrumentado(filename, init, maxi, inc):
    file = open(filename, 'w')
    file.write('n;time_while;time_for\n')
    for n in range(init, maxi, inc):
        a = list(range(n))
        x = n
        file.write(f'{n};{buscar_while_instrumentado(x, a)};{buscar_for_instrumentado(x, a)}\n')
    file.close()
test_buscar_instrumentado('buscar_instrumentado.csv', 10, 200, 10)