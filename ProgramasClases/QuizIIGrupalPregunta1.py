'''
Pregunta #1
Nombre: Victor David Coto Solano / ID: 305440064
Nombre: Diego Quiros Artinano / ID: 901150326
Nombre: Derek Rojas Mendoza / ID: 604740973
'''

def has_peak(a:'list[int]') -> bool:
    n = len(a)
    if n <= 1:
        return False
    if n == 2:
        return a[0] < a[1] 
    if n == 3:
        return a[0] < a[1] and a[1] < a[2]
    m = len(a) // 2
    return has_peak(a[:m]) or has_peak(a[m:])

a = [9,8,7,6,5,4,3,2,1]
b = [1,2,3,4,5,6,7,8,9]
c = [9,8,7,6,7,8,9,8,7,5]
d = [9,8,7,6,7,6,5,4,3,2,1]
e = [0,0,1,2,3,0,0,0,0,0,0,0] #False for some reason
f = [0,0,0,1,2,3,0,0,0,0,0,0] 
g = [0,0,0,0,1,2,3,0,0,0,0,0] 
h = [0,0,0,0,0,1,2,3,0,0,0,0]
i = [0,0,0,0,0,0,1,2,3,0,0,0]
j = [0,0,0,0,0,0,0,1,2,3,0,0]
k = [0,0,0,0,0,0,0,0,1,2,3,0]
l = [0,0,0,0,0,0,0,0,0,1,2,3]
# print(has_peak(a)) #False
# print(has_peak(b)) #True
# print(has_peak(c)) #True
# print(has_peak(d)) #False
# print(has_peak(e)) # todo False
# print(has_peak(f)) #True
# print(has_peak(g)) #True
# print(has_peak(h)) # todo False
# print(has_peak(i)) #True
# print(has_peak(j)) #True
# print(has_peak(k)) # todo False
# print(has_peak(l)) #True

def has_peak_v2(a:'list[int]'):
    def dyc(a, b):
        ocurre = False
        for i in range(1, len(a)):
            ocurre = a[i-1] < a[i] and a[i] < a[i+1]
        if not ocurre:
            for i in range(1, len(b)):
                ocurre = b[i-1] < b[i] and b[i] < b[i+1]
        return ocurre
    n = len(a)
    if n <= 1:
        return a
    m = n // 2
    return dyc(has_peak_v2(a[:m]), has_peak_v2(b[m:]))

print(has_peak_v2(a)) #False
print(has_peak_v2(b)) #True
print(has_peak_v2(c)) #True
print(has_peak_v2(d)) #False
print(has_peak_v2(e)) # todo False
print(has_peak_v2(f)) #True
print(has_peak_v2(g)) #True
print(has_peak_v2(h)) # todo False
print(has_peak_v2(i)) #True
print(has_peak_v2(j)) #True
print(has_peak_v2(k)) # todo False
print(has_peak_v2(l)) #True