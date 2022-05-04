# intento de hacer busqueda binaria, mi version

def busqueda_binaria(a:'list[int]', x:int)-> int:
    if len(a) == 0:
        return -1
    n = (len(a)-1)//2
    # print(f"{n},{a[n]}")
    if a[n] == x:
        return n
    elif a[n] > x:
        return busqueda_binaria(a[:n], x)
    elif a[n] < x:
        test = busqueda_binaria(a[n+1:], x)
        if test != -1:
            return n+1 + test
        else:
            return test
    

a = [1,2,3,4,5,6,7,8]
x = 8
print(f"{a},{busqueda_binaria(a, x)}")

a = [8,9,10,11,12,13,14,15,16]
print(f"{a},{busqueda_binaria(a, x)}")

a = [5,6,7,8,9,10,11,12]
print(f"{a},{busqueda_binaria(a, x)}")

a = [0,1,2,3,4,5,6,7]
print(f"{a},{busqueda_binaria(a, x)}") # This is not working because it will return -1 + all the n + 1's that appear

a = [9, 10, 11, 12, 13, 14, 15, 16, 17]
print(f"{a},{busqueda_binaria(a, x)}") #This does work because I am not adding anything after the slice

# version del profe

def busbin(x, a):
    def buscando(left, right):
        if left > right:
            return -1 #not found
        m = (left + right) // 2
        if x == a[m]:
            return m # Bingo! Found at point m
        if x < a[m]:
            return buscando(left, m-1)
        return buscando(m+1, right)
    #Start searching
    return buscando(0, len(a) -1)