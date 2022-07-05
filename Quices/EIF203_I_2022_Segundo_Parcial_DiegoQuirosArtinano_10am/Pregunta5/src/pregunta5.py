"""
    Model to 'pregunta 5'
    loriacarlos@gmail.com
    EIF203 I-2022
    Might require Anaconda environment (conda activate)
    
    Author: Diego Quiros Artinano
    ID: 901150326
    NRC: 41XXX
"""
import networkx as nx
import numpy as np
import sys
import matplotlib.pyplot as plt


test_graph = '../demo_data/grafo_5.graphml'

def convert_graph_to_matrix(g, dtype= np.int64):
    """
        Convierte en grafo en una matrix de numpy
        Los nodos ahora son índices en el orden alfabetico de g.nodes().
        Por ejemplo: si 'A','B', ..., 'V' son los nodos 'A' es indice 0, ..., 'V' es 21
        Use el metodo index de list para obtener el indice de un nodo        
    """
    return nx.to_numpy_array(g, dtype=dtype).view(np.matrix)
    
def paths_from_to(g, v, w, m=1, n=10):
    """
        g: grafo de networkx
        v, w: vertices en g (debe validarse)
        m, n: enteros mayores o guales a 1.
        Encuentra numero de caminos de largo m o largo n de v a w en g
        Retorna un tuple (largo_m, largo_n) donde largo_m y largo_n son los caminos de largo m y n respectivamente
    """
    # 0) Asuma que m y n son enteros tales que 1 <= m y 1 <= n (no lo valide)
    V = list(g.nodes())
    # 1) Validar que v y w son vertices de g. Retorna -1 si no se cumple
    #    Usando index determinar el indice en V de v y w
    if v not in V and w not in V:
        return -1
    mTimes = m
    m = convert_graph_to_matrix(g)
    
    # print(m) # 2) eliminar este print una vez resuelto el problema
    # 3) Escribir su respuesta a continuación

    def exponentiateMatrix(m, e):
        exponentiatedMatrix = m
        for i in range(e-1):
            exponentiatedMatrix = np.matmul(exponentiatedMatrix, m)
        return exponentiatedMatrix

    mExponentiatedM = exponentiateMatrix(m, mTimes)
    mExponentiatedN = exponentiateMatrix(m, n)

    # return result # Retorna un tuple (largo_m, largo_n)
    # return (mCounter, nCounter)

    return (mExponentiatedM[ord(v)-65, ord(w)-65], mExponentiatedN[ord(v)-65, ord(w)-65])
    raise BaseException("paths_from_to not yet implemented") # 4) Eliminar este raise una vez implementado

def test_paths_from_to(graph_path=test_graph, v='A', w='R', m=1, n=10):
    """
        Prueba pregunta 5
    """
    print(f"*** Testing 'Pregunta 5' with '{graph_path}' {v=:}, {w=:}, {m=:} {n=:} ****\n")
    g = nx.read_graphml(graph_path)
    nx.draw(g, with_labels=True)
    plt.show()
    result = paths_from_to(g, v, w, m, n)
    print(f"{result=:}")
    
your_NNNN_HH = "DiegoQuirosArtinano 10am"   # Poner su Nombre y horario
if __name__ == "__main__":
    print(f"\n>>> Testing Script authored by '{your_NNNN_HH}' <<<\n")
    argv = sys.argv
    try:
        test_paths_from_to(argv[1] if len(argv)  == 2 else test_graph)
    except BaseException as e:
        print( f"\n*** Test Failed! Reason: {e} by '{your_NNNN_HH}' ***" )
    
        