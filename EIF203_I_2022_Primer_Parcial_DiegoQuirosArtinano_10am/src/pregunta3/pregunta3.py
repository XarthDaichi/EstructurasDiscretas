'''
Nombre: Diego Quiros Artinano
Cedula: 901150326 / ID-Universidad: 315071
NRC: 41712
'''
from typing import Any
def mas_larga_anidada(a:'list[Any]') -> 'list[Any]':
    largest = a
    for i in a:
        if type(i) == list:
            temp = mas_larga_anidada(i)
            if len(largest) < len(temp):
                largest = temp
    return largest

a = [[1,1,[1,1,1,1,1,1,1]],[],[1]]
print(mas_larga_anidada(a))