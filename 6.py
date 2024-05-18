
A = int(input("kiriting A "))
N = int(input("kiriting N "))

while N <= 0:
	N = int(input("kiriting N "))

mul = 1

for x in range(1,N+1):
	mul = mul * A

print(A,'^',N,'=',mul)