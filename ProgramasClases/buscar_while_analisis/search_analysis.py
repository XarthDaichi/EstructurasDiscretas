# def buscar_while(x:int, a:'list[int]')-> int:
#     p:int = 0
#     while p < len(a):
#         if x == a[p]:
#             return p
#         else:
#             p += 1
#     return -1
'''
Analisis 6-pasos de buscar_while
PASO-1: Tamano de dators (n)
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
def buscar_while_instrumentadoOriginal(x:int, a:'list[int]')-> int:
    contador_operaciones = 0
    p:int = 0
    contador_operaciones += 1 # =
    while p < len(a):
        contador_operaciones += 2 # < y len
        if x == a[p]:
            contador_operaciones += 2 # == y []
            return contador_operaciones
        else:
            p += 1
            contador_operaciones += 3 # == y [] y +=
    contador_operaciones += 2 # < y len
    return contador_operaciones

def test_buscar_while_instrumentadoOriginal(filename, init, maxi, inc):
    file = open(filename, 'w')
    file.write('n;time\n')
    for n in range(init, maxi, inc):
        a = list(range(n))
        x = n
        file.write(f'{n};{buscar_while_instrumentadoOriginal(x, a)}\n')
    file.close()
test_buscar_while_instrumentadoOriginal('buscar_while_instrumentadoOriginal.csv', 10, 200, 10)

def buscar_while_instrumentado_profe(x:int, a:'list[int]')-> int:
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

def test_buscar_while_instrumentado_profe(filename, init, maxi, inc):
    file = open(filename, 'w')
    file.write('n;time\n')
    for n in range(init, maxi, inc):
        a = list(range(n))
        x = n
        file.write(f'{n};{buscar_while_instrumentado_profe(x, a)}\n')
    file.close()
test_buscar_while_instrumentado_profe('buscar_while_instrumentado_profe.csv', 10, 200, 10)

def buscar_while_instrumentado_sinlena(x:int, a:'list[int]')-> int:
    contador_operaciones = 0
    p:int = 0
    contador_operaciones += 1
    final:int = len(a)
    contador_operaciones += 1
    while p < final:
        contador_operaciones += 1
        if x == a[p]:
            contador_operaciones += 2
            return contador_operaciones
        else:
            p += 1
            contador_operaciones += 3
    contador_operaciones += 1
    return contador_operaciones
def test_buscar_while_instrumentado_sinlena(filename, init, maxi, inc):
    file = open(filename, 'w')
    file.write('n;time\n')
    for n in range(init, maxi, inc):
        a = list(range(n))
        x = n
        file.write(f'{n};{buscar_while_instrumentado_sinlena(x, a)}\n')
    file.close()
test_buscar_while_instrumentado_sinlena('buscar_while_instrumentado_sinlena.csv', 10, 200, 10)
        