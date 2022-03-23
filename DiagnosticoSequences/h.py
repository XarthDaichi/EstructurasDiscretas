times = int(input('Enter the number of sequence: '))
if times is 0:
    print('b')
else:
    print("a^" + str(times * (times+1) // 2) + ' *b')