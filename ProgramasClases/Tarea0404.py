from typing import Any
def largo_lista(a:'list[Any]') -> int:
    if a == []:
        return 0
    return 1 + largo_lista(a[1:])

a = []
for i in range(100):
    a.append(1)

print(largo_lista(a))

def largo_lista_instrumentado(a:'list[Any]') -> int:
    operaciones = 0
    if a == []:
        return operaciones
    operaciones += 1 #el + del return
    return operaciones + largo_lista_instrumentado(a[1:])

print(largo_lista_instrumentado(a))

'''
PASO-1
n depende de len(a)
n=len(a)

PASO-2
T+

PASO-3
T_largo_lista(0) = 0
T_largo_lista(n) = 1 + T_largo_lista(n-1)

PASO-4
T_largo_lista(n) = n

PASO-5
O(n)

PASO-6
instumentado esta arriba termina siendo n = operaciones entonces grafica identidad
'''

def buscar_en_anidada(x:int, a:'list[Any]') -> bool:
    for i in a:
        if type(i) == int:
            if x == i: return True
        elif type(i) == list:
            if buscar_en_anidada(x, i):
                return True
    return False

a1 = []
a2 = [1, 2, 3]
a3 = [[]]
a4 = [1, [[]], [2]]
a5 = [[1, 2, 3], 4]
a6 = [[], 1]
a7 = [[[1, 2, [3]]], 4, [5]]
a8 = [1, [2], [2, [3, [4]]]]

print(buscar_en_anidada(1, a1))
print(buscar_en_anidada(1, a2))
print(buscar_en_anidada(2, a3))
print(buscar_en_anidada(2, a4))
print(buscar_en_anidada(3, a5))
print(buscar_en_anidada(1, a6))
print(buscar_en_anidada(3, a7))
print(buscar_en_anidada(4, a8))

'''
Escribauna función recursiva  buscar_en_anidada(x:int, a:list[Any]) -> bool  que reciba una lista anidada (de números) a y retorne True si x ocurre en alguna parte en la lista a Retorna False si no ocurre.
Notas importantes:
1) Este ejercicio puede ser "peludillo" (jerga: no tan fácil). Tal vez quiera intentarlo después de haber calentado primero con otros ejercicios
2) Puede usar  la función type para saber el tipo de un objeto. 
Por ejemplo type(x) == int para saber si x es un número. O type(x) == list para saber si x es una lista.
3) Para usar el tipo Any escriba al inicio de su módulo el siguiente import: 
from typing import Any
'''