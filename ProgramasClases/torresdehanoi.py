def hanoi(n, A='A', B='B', C='C'):
    if n == 1:
        print(f"Mueva de {A} a {C}") # moviendo el unico disco en A hasta C
        return
    hanoi(n-1, A, C, B)          # moviendo n-1 discos de A hasta B
    print(f"Mueva de {A} a {C}") # moviendo el unico disco de A a C
    hanoi(n-1, B, A, C)          # moviendo n -1 discos de B hasta C