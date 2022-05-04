'''
1) Considere este algoritmo recursivo que suma los elementos de una lista de números
def sumar(a: list[int]) -> int:
    if a == []:
        return 0
    return a[0] + sumar(a[1:])
Donde a[1:] es llamado un slice (porción) de a, es decir, una lista que es una copia de a quitando el primer elemento.
(En general a[i:j] es la sublista de a desde posición i hasta posición j-1. Si j no se pone se asume que el slice llega hasta el final. Si no hay slice posible se devuelve [].
Por ejemplo: Si a=['a','b','c','d', 'e']
a[1:] es ['b','c','d', 'e']
a[2:4] es ['c','d']
a[3:] es ['d', 'e']
(hay otras variantes vacilonas, por ejemplo con negativos, que Ud. puede investigar por su cuenta. por ejemplo este blog es muy bueno. Hay otros. No es obligación profundizar sobre slices, es solo por si quiere aprender más de lo que voy a pedir. Son muy divertidos y poderosos)
a) Estudie y entienda como trabaja sumar. Haga casos de prueba
b) Asuma que a[1:] toma tiempo n - 1 operaciones internas (en C) cada una de tiempo 1 si len(a) == n.
Sea [1:] la operación de interés. Haga el análisis 6 pasos de sumar.
c) ¿A cuántos registros INFO-sumar (como los llamamos en la clase al explicar stack y recursión) se les hace push en el stack de Python para una lista de n elementos?
'''

def sumar(a: 'list[int]') -> int:
    if a == []:
        return 0
    return a[0] + sumar(a[1:])

'''
PASO-1:
Cantidad de Datos n = len(a)

PASO-2:
T==
T[]
T+
T[1:]
Todos se van a considerar constantes y todos 1 igual al mayor
Profe dijo que a[1:] es la unica que se va a contar para este analisis

PASO-3:
a[1:], solo aparece una vez en el ultimo return, entonces solo se le suma 1 a las operaciones
T(0) = 0
T(n) = 1 + T(n-1)

PASO-4:
T (n) = 1 + 1 + 1 + ... + 1 + 1 + 1 + 0 <-- n veces 1
T (n) = n

PASO-5:
O(n)

PASO-6:
'''

def sumar_instrumentado(a: 'list[int]') -> int:
    operaciones = 0
    if a == []:
        return operaciones
    operaciones += 1
    return sumar(a[1:])

# La ecuacion va a dar lineal identidad

'''
La cantidad de veces que hace push es n veces (todos los n-1 hasta e incluyendo 0)
'''