import timeit
setup = ' '
'''
Cual es el tiempo de corrida del siguiente algoritmo mayor(x,y) que calcula el mayor entre dos numeros x y y? Asuma que >= (mayor o igual) es la operacion de interes
'''
profe_mayor = '''
def mayor(x, y):
    if x >= y: return x
    else: return y
'''
def mayor(x, y):
    if x >= y: return x
    else: return y

def mayor_instrumentado(x, y):
    operaciones = 0
    if x >= y: 
        operaciones += 1
        return operaciones
    else: 
        operaciones += 1
        return operaciones
    
# El instrumentado en todo va a dar 1 porque solo entra y sale del if
print("Tiempo de mayor_profe: ", timeit.timeit(stmt = profe_mayor, number = 10000))
'''
Mejora de estilo: Use el equivalente en Python del operador ternario(?:) de C++ y reescriba la funcion mayor. Mejora eso el tiempo de corrida? Explique.
'''
my_mayor = '''
def mayor_mejorado(x, y):
    return (x if x >= y else y)
'''
def mayor_mejorado(x, y):
    return (x if x >= y else y)
'''
Esta pasando por la misma cantidad de operaciones siempre cuenta una vez el >= entonces deberia dar el mismo
'''
print("Tiempo de mayor_my: ", timeit.timeit(stmt = my_mayor, number = 10000))
'''El timeit dan resultados muy similares'''


'''
Asuma que cambiamos el algoritmo mayor por mayor2 (or es como || en C++).
Asuma, sólo hipotéticamente, que cualquier operación entre >=, ==, or, = toma 2𝑥10−8
segundos cada una en una cierta computadora. ¿Cuántas veces es mejor mayor que
mayor2 en dicha computadora? Asuma el peor caso.
'''

def mayor2(x, y):
    m = None # None es el valor vacio (void) en python
    if x == y or x > y:
        m = x
    else:
        m = y
    return m

def mayor2_instrumentado(x, y):
    operaciones = 0
    m = None
    operaciones += 1
    if x == y or x > y:
        operaciones += 3
        m = x
        operaciones += 1
    else:
        operaciones += 3
        m = y
        operaciones += 1
    return m

''' 
El mayor 2 dura 5 operaciones cada vez que corre, el cual es 5 * 2 * 10^-8 => 10^-7 => 0.0000001
El mayor dura 1 operacion cada vez que corre 2 * 10^-8                              => 0.00000002
Esto significa que en ningun caso es mejor el mayor2
'''

'''
Cual es el O-grande de T_mayor(n)? El de T_mayor2(n)?
El tamano de datos no le cambia las operaciones
Ecuacion T_mayor(n) = 1
Ecuacion T_mayor(n) = 5
de los dos es O(1) O-constante
'''

'''
Cual es el tiempo de corrida de la funcion maxima(a) siguiente siendo a una lista de numeros? Use < como la operacion de interes (Use el metodo de los 6 pasos de analisis)
'''

def maximo(a):
    """
    Asuma que a es un arreglo de numeros no vacio
    es decir que len(a) > 0
    """
    m = a[0]
    # operaciones = 0
    for i in range(1, len(a)):
        #operaciones += 1
        if m < a[i]:
            m = a[i]
    return m

'''
PASO-1
Cantidad de datos depende del len(a)
n = len(a)

PASO-2
Operaciones de interes
T<

PASO-3
T_maximo(1) = 0
T_maximo(n) = n-1 + T_maximo(n-1)

PASO-4
T_maximo(n) = n-1 + n-2 + n-3 + ... + 2 + 1 + 0
t_maximo(n) = n(n-1)/2

PASO-5
O(n)

PASO-6
instrumentado con comentarios en el codigo de arriba
'''

'''
Escriba un algoritmo que encuentre el máximo y el mínimo de una lista de números. No
use ni max ni min de Python, haga su propia versión. ¿Cuál es el tiempo de corrida de su
solución? Compare con una solución que busca primero el mínimo y luego busca el
máximo en búsquedas independientes.
'''

def minimo(a):
    m = a[0]
    for i in range(1, len(a)):
        temp = a[i]
        if m > temp:
            m = temp
    return m

maximo = '''
def maximo(a):
    m = a[0]
    for i in range(1, len(a)):
        temp = a[i]
        if m < temp:
            m = temp
    return m
'''

minimo = '''
def minimo(a):
    m = a[0]
    for i in range(1, len(a)):
        temp = a[i]
        if m > temp:
            m = temp
    return m
'''

print("Tiempo de minimo: ", timeit.timeit(stmt=maximo, number=10000))
print("Timepo de minimo: ", timeit.timeit(stmt=minimo, number=10000))

'''
Estudie con cuidado el siguiente algoritmo recursivo (no hace nada especial o conocido, es
sólo un ejercicio). Usando print como la función de interés calcule analíticamente el
tiempo de corrida (método de cinco pasos explicado en clase). Después verifique
empíricamente su resultado.
'''

def f(n):
    if n == 0:
        for i in range(0, 5, 2):
            print('FINAL')
        return
    print('ANTES')
    f(n-1)
    for i in range(n):
        print('DESPUES')
        
# print (f(10))
'''
PASO-1
datos depende de n = n

PASO-2
Operaciones de interes
Tprint

PASO-3
T_f(0) = 3
T_f(n) = 1 + n + T_f(n-1)

PASO-4
T_f(n) = n + n(n+1)/2 + 3

PASO-5
O(n^2)

PASO-6
'''

def f_instrumentado(n):
    operaciones = 0
    if n == 0:
        for i in range(0, 5, 2):
            operaciones += 1
            print('FINAL', operaciones)
        return operaciones
    operaciones += 1
    print('ANTES', operaciones)
    operaciones += f_instrumentado(n-1)
    for i in range(n):
        operaciones += 1
        print('DESPUES', operaciones)
    return operaciones
        
print("f_instrumentado", f_instrumentado(9)) # deberia dar 57

'''
Analice y determine el tiempo de corrida de la función buscar(x, a) donde a es un
arreglo de números y x un número a buscar en a. Use == y >= ambas como las
operaciones de interés asumiendo que cada una toma 1 unidad de tiempo (la misma para
ambas). Asuma el peor caso, indicando en su respuesta cuándo ocurre el peor caso. Note
que en Python una función puede tener definidas internamente funciones, que son
“privadas” a la función que las contiene.
'''

def buscar(x, a):
    n = len(a)
    def buscando(i):
        if i >= n: return -1
        if x == a[i]: return i
        return buscando(i+1)
    #Llama a buscando
    return buscando(0)

'''
PASO-1
n depende de len(a)
n = len(a)

PASO-2
T==
T>=

PASO-3
T_buscar(0) = 1
T_buscar(n) = T_buscar(0) + buscar(1)

PASO-4
T_buscar(n) = 1 + 2 + 2 + 2 + ... 2
T_buscar(n) = 2n + 1

PASO-5
O(n)

PASO-6
'''

def buscar_instrumentado(x, a):
    n = len(a)
    def buscando(i):
        operaciones = 0
        operaciones += 1
        if i >= n: return operaciones
        operaciones += 1
        if x == a[i]: return operaciones
        return operaciones + buscando(i+1)
    #Llama a buscando
    return buscando(0)
a = []
for i in range(100):
    a.append(1)
    
print(buscar_instrumentado(2,a))


'''
Definición: “Recursión de cola” es cuando las llamadas de una función recursiva nunca
quedan “atrapadas” como argumentos de otras operaciones ni dejan esperando cálculos
después de alguna llamada recursiva. Por ejemplo, la anterior función buscando es
recursiva de cola, pero la función que se muestra abajo, exponenciar , no es recursiva
de cola, porque la llamada recursiva queda atrapada como un argumento de *. Diseñe e
implemente en Python una versión recursiva de cola para 𝑛!. Llámela fcola(n).
Sugerencia: Use la misma idea que se aprecia en buscando. Pruebe la correctitud de
fcola, por inducción en los naturales: es decir: ∀𝑛: 𝑓𝑐𝑜𝑙𝑎(𝑛) = 𝑛!. Nota: Cuando una
recursividad no es de cola, la misma va a ocupar una pila (stack) para guardar los registros
de activación, o stack frames. Por eso se le llama también recursión de pila.
'''

def fcola(n):
    def f(i):
        if i == 1: return 1
        return f()
    return f(n)

print(fcola(3)) 