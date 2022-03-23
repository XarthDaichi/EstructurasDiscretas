times = int(input('Enter the number of sequence: '))
if times is 0:
    print(1)
else:
    factorial = 1
    for i in range(2, times + 1):
        factorial *= i
    print(factorial)