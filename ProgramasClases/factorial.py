def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def test(times = 10):
    for n in range(times):
        print(factorial(n))