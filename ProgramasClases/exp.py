def exp_recursivo(x,n): # Hacia atras
    if n == 0:
        return 1
    return x * exp_recursivo(x,n-1)

def exp_iterativa(x, n): # Hacia adelante
    resultado = 1
    for i in range(n):
        resultado *= x
    return resultado

def test_exp(times = 10, x = 2):
    for n in range(times):
        print(n,exp_iterativa(x, n), exp_recursivo(x, n))
test_exp()