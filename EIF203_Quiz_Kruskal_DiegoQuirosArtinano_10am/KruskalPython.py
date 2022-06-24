import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def kruskal(V, E):
    
    TGraph = nx.Graph()
    TGraph.add_nodes_from(V)
    
    T = []
    
    def sort(E):
        n = len(E)
        for i in range(n):
           for j in range(n-i):
               a = E[j]
               if a != E[-1]:
                   b = E[j+1]
                   if a[2] > b[2]:
                       E[j] = b
                       E[j+1] = a
        return E

    def find(i):
        return nx.has_path(TGraph, i[0], i[1])

    E = sort(E)
    print
    for i in E:
        if not find(i):
            T += [i]  
            TGraph.add_edge(i[0], i[1])
    return T
                
a='a'
b='b'
c='c'
d='d'
e='e'
f='f'
g='g'

V1 = [a,b,c,d,e]
E1 = [[a,b,10], [a,e,100], [a,d,30], [b,c,50], [c,d,20], [c,e,10], [d,e,60]]

print(kruskal(V1,E1))

print()

V2 = [a,b,c,d,e,f,g]
E2 = [[a,b,4], [a,c,9], [a,d,3], [b,c, 5], [b,f, 7], [c,d, 1], [c,e,6], [d,e,2], [d,g,4], [e,f,8], [e,g,7], [f,g, 2]]
print(kruskal(V2, E2))