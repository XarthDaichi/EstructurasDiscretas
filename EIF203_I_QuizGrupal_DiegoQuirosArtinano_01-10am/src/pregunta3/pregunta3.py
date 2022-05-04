'''
Nombre: Diego Quiros Artinano
Cedula: 901150326 / ID-Universidad: 315071
NRC: 41712
'''

# # El codigo hecho en clase
# def busbin(x, a):
#     def buscando(left, right):
#         if left > right:
#             return -1 #not found
#         m = (left + right) // 2
#         if x == a[m]:
#             return m # Bingo! Found at point m
#         if x < a[m]:
#             return buscando(left, m-1)
#         return buscando(m+1, right)
#     #Start searching
#     return buscando(0, len(a) -1)

def busbin_instrumentado(x, a):
    def buscando(left, right):
        operaciones = 0
        if left > right:
            return operaciones
        m = (left + right) // 2
        operaciones += 1 # el == de la siguiente linea
        if x == a[m]:
            return operaciones 
        operaciones += 1 # el < que sigue
        if x < a[m]:
            return operaciones + buscando(left, m-1)
        return operaciones + buscando(m+1, right)
    return buscando(0, len(a) -1)


def test_busbin_instrumentado(filename, start, end, inc):
    file = open(filename, 'w')
    file.write('n;time\n')
    for n in range(start, end, inc):
        a = list(range(2**n))
        x = 2**n
        file.write(f'{n};{busbin_instrumentado(x, a)}\n')
    file.close()
test_busbin_instrumentado('busbin_instrumentado.csv', 2, 9, 1)