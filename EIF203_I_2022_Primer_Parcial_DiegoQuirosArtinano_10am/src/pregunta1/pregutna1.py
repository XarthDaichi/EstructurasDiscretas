'''
Nombre: Diego Quiros Artinano
Cedula: 901150326 / ID-Universidad: 315071
NRC: 41712
'''
# parte b)
def s_rec(n:int)-> int:
    if n == 0: return 0
    if n == 1: return -5
    return 6* s_rec(n-2) - 5 * s_rec(n-1) + 3 * n

# print(s_rec(4)) verificando que diera la misma respuesta que la a)

# parte d)
def s_iter(n:int)-> int:
    prev_last = 0
    last = -5
    s = 0
    for i in range(2, n+1):
        s = 6 * prev_last -5 * last + 3 * i
        prev_last = last
        last = s
    return s

print(s_iter(4))
