times = int(input('Enter the number of sequence: '))
sequence = []
for i in range(times):
    if i is 0 or i is 1:
        sequence.append(1)
    else:
        sequence.append(sequence[i-1] + sequence[i-2])
print(sequence)
sum = 0
for i in range(times):
    sum += sequence[i]
print(sum)