def es_simetrica(a:'list[list[int]]')-> bool:
    # counter = 0
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            # counter += 1
            # print(counter,': ', i, j, a[i][j], a[j][i])
            if a[i][j] != a[j][i]:
                return [i, j]
    return True

# # a = [[1,2,3],[4,5,6],[7,8,9]]
# a = [[1,1,1],[1,1,1],[1,1,1]]
# b = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# c = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# d = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
# f = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]

# print(es_simetrica(a))
# print(es_simetrica(b))
# print(es_simetrica(c))
# print(es_simetrica(d))
# print(es_simetrica(f))

def es_simetrica_instrumentado(a:'list[list[int]]')-> int:
    contador_operaciones:int = 0
    n = len(a)
    contador_operaciones += 3 # range de afuera y el = n y el len(a)
    for i in range(n - 1):
        contador_operaciones += 1 # cada range nuevo cuando cambia el i
        for j in range(i + 1, n):
            contador_operaciones += 5 # 2 != y 4 []'s
            if a[i][j] != a[j][i]:
                return contador_operaciones
    return contador_operaciones

def test_simetrica_instrumentado(filename, init, maxi, inc):
    file = open(filename, 'w')
    file.write('n;time\n')
    for n in range(init, maxi, inc):
        a = []
        for i in range(n):
            a.append([])
            for j in range(n):
                a[i].append(1)
        file.write(f'{n};{es_simetrica_instrumentado(a)}\n')
    file.close()
test_simetrica_instrumentado('simetrica_instrumentado.csv', 10, 200, 10)

# for n in range(10, 30, 10):
#         a = []
#         for i in range(n):
#             a.append([])
#             for j in range(n):
#                 a[i].append(1)
#         print(a)
#         print()