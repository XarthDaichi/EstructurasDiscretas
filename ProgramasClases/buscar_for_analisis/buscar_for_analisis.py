def buscar_for_instrumentado(x:int, a:'list[int]') -> int:
    contador_operaciones = 0
    contador_operaciones += 2 #crear range y la asignacion del len
    for p in range(len(a)): #asignar p, verificar tamano
        contador_operaciones += 2 # las dos cosas del if
        if x == a[p]:
            return contador_operaciones#ultima verificacion
    return contador_operaciones

def test_buscar_for_instrumentado(filename, init, maxi, inc):
    file = open(filename, 'w')
    file.write('n;time\n')
    for n in range(init, maxi, inc):
        a = list(range(n))
        x = n
        file.write(f'{n};{buscar_for_instrumentado(x, a)}\n')
    file.close()
test_buscar_for_instrumentado('buscar_for_instrumentado.csv', 10, 200, 10)