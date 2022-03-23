def buscar(x, a):
    for p in a:
        if x == a[p]:
            return p
    return -1
a = [-1, 20, 8, 3, 5]
print(buscar(8, a))
