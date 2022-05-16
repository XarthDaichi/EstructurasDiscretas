A = set(range(0,10))
print(A)

print(type(A))
L = [1,2,1,3,2,10]
print(L)

S = {1,2,1,3,2,10}
print(S)

print(1 in S)
print(1 in L)

for x in S: print(x)

ParesEnA = [n for n in A if n % 2 == 0]
print(ParesEnA)

B = list('abc')
print(B)

AxB =[(a, b) for a in A for b in B]
print(AxB)

R = [(a,b) for a in A for b in B if a % 2 == 0 and b == 'a' or b == 'c']
print(R)

R = [(a,b) for a in A for b in B if a % 2 == 0 and (b == 'a' or b == 'c')]
print(R)

R = [(a, b) for a in ParesEnA for b in B if b == 'a' or b == 'c']
print(R)

R = [(a,b) for a in ParesEnA for b in B if b in ['a', 'c']]
print(R)

Person = ['ana', 'pedro', 'juan', 'maria']
Course = ['eif101','eif102','mat300']
llevaCurso = [{'ana', 'eif101'}, {'ana', 'mat300'}, {'pedro', 'eif102'}, {'juan', 'mat300'}, {'maria', 'mat300'}]