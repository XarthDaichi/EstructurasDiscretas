times = int(input('Enter the number of sequence: '))
if times is 0:
    print(0)
else:
    print(times * (times + 1) * (2 * times + 1) // 6)
