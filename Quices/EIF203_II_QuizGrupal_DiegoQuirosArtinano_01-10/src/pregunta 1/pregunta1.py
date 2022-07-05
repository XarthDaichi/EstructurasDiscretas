'''
Pregunta #1
Nombre: Victor David Coto Solano / ID: 305440064
Nombre: Diego Quiros Artinano / ID: 901150326
Nombre: Derek Rojas Mendoza / ID: 604740973
'''

def has_peak(a:'list[int]') -> bool:
    if len(a) <= 1:
        return False
    if len(a) == 2:
        return a[0] < a[1]
    m = len(a) // 2
    return has_peak(a[:m]) or has_peak(a[m:])  

a = [9,8,7,6,5,4,3,2,1]
b = [1,2,3,4,5,6,7,8,9]
c = [9,8,7,6,7,8,9,8,7,5]
print(has_peak(a))
print(has_peak(b))
print(has_peak(c))