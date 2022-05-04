'''
Nombre: Diego Quiros Artinano
Cedula: 901150326 / ID-Universidad: 315071
NRC: 41712
'''
def g_instrumentado(n):
    operaciones = 0
    print('Start')
    operaciones += 1
    for i in range(0, 2 * n + 1):
        print(i)
        operaciones += 1
    for i in range(n, -1, -1):
        for j in range(2 * i):
            print(i, j)
            operaciones += 1
            print()
            operaciones += 1
    print('End')
    operaciones += 1
    return operaciones
def test_g_instrumentado(filename, init, maxi, inc):
    file = open(filename, 'w')
    file.write('n;time\n')
    for n in range(init, maxi, inc):
        file.write(f'{n};{g_instrumentado(n)}\n')
    file.close()
test_g_instrumentado("pregunta2.csv", 10, 200, 10)
    
    