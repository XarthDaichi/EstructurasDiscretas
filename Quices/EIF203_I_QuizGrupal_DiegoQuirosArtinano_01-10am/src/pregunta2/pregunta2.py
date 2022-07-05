"""
Derek Rojas Mendoza
604740973
Grupo: 10am
"""

def g_formula(n):
    cont = 0
    if n == 0:
        print('FIN')
        cont += 1
        return cont
    for i in range(10, 17, 2):
        cont += g_formula(n - 1)
    print()
    cont += 1
    return cont
print(g_formula(2))
"""
Analisis de losmprimeros 5 pasos
Paso 1: Criterio de crecimiento dado por n
Paso 2: Funcion de interes: print
Paso 3: 4Fn-1 + 1
Paso 4: 4^n + (4^n - 1) / (4 - 1)
paso 5: O(4^n+1)
"""