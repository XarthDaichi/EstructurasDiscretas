# Un modulo para buscar
'''
    Modulo para buscar para estudiar busqueda secuencial
    diegoqahh@gmial.com
    14/03/2022
    tambien puedo usar tres " para el comentario de varias lineas
'''

autor = 'diegoqahh@gmail.com' # autor:str = 'diegoqahh@gmail.com'  Type hint (sugerencia de tipo)

def buscar_while(x:int, a:'list[int]') -> int:
    print('Arranca buscar')
    p:int = 0
    while p < len(a):
        if x == a[p]:
            return p
        else:
            p += 1
    
    return -1

def buscar_for(x:int, a:'list[int]') -> int:
    print('Arranca buscar')
    for p in range(len(a)):
        if x == a[p]:
            return p
    
    return -1

# Ejercicio 1 Tarea 2
def buscar_in(x:int, a:'list[int]')-> int:
    if x in a:
        return a.index(x)
    return -1

# Ejercicio 2 Tarea 2
def buscar_while_desde(x:int, a:'list[int]', desde:int, hasta:int) -> int:
    p:int = desde
    while p < hasta:
        if x == a[p]:
            return p
        else:
            p += 1
    return -1

# Ejercicio 3 Tarea 2
def buscar_for_desde(x:int, a:'list[int]', desde:int, hasta:int)-> int:
    for p in range(desde, hasta):
        if x == a[p]:
            return p
    return -1

# Ejercicio 4 Tarea 2
def buscar_index(x:int, a:'list[int]')-> int:
    try:
        return a.index(x)
    except:
        return -1

# Ejercicio 5 Tarea 2
def buscar_while_desdeV2(x:int, a:'list[int]', desde:int, hasta:int) -> int:
    p:int = desde
    inOrDe:int = 1
    if desde > hasta:
        inOrDe = -1
    while p < hasta:
        if x == a[p]:
            return p
        else:
            p += inOrDe
    return -1

# Ejercicio 6 Tarea 2
def buscar_for_desdeV2(x:int, a:'list[int]', desde:int, hasta:int)-> int:
    inOrDe = 1
    if desde > hasta:
        inOrDe = -1
    for p in range(desde, hasta, inOrDe):
        if x == a[p]:
            return p
    return -1

print('buscar procesado')

def test_buscar():
    print('*** Probando buscar ***')
    print('Primera prueba while')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_while(x,a)}")
    
    print('Segunda prueba while')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_while(x,a)}")
    
    print('Primera prueba for')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_for(x,a)}")
    
    print('Segunda prueba for')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_for(x,a)}")
    
    print('Primera prueba in')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_in(x,a)}")
    
    print('Segunda prueba in')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_in(x,a)}")
    
    print('Primera prueba while desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_while_desde(x,a,0,4)}")
    
    print('Segunda prueba while desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_while_desde(x,a,1,3)}")
    
    print('Primera prueba for desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_for_desde(x,a,0,4)}")
    
    print('Segunda prueba for desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_for_desde(x,a,1,3)}")
    
    print('Primera prueba index')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_index(x,a)}")
    
    print('Segunda prueba index')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_index(x,a)}")
    
    print('Primera prueba while desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_while_desdeV2(x,a,4,0)}")
    
    print('Segunda prueba while desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_while_desdeV2(x,a,3,1)}")
    
    print('Primera prueba for desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 8
    print(f"x={x} en a={a} ocurre en posicion {buscar_for_desdeV2(x,a,4,0)}")
    
    print('Segunda prueba for desde')
    a = [20, 3, 5, 87, 10, 8, 0]
    x = 666
    print(f"x={x} en a={a} ocurre en posicion {buscar_for_desdeV2(x,a,3,1)}")
    
    print('*** Termina la prueba ***')
    
test_buscar()