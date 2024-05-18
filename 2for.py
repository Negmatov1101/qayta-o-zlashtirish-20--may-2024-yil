
A = int(input("Kiriting A "))
N = int(input("Kiriting N "))

while N <= 0:
	N = int(input("Kiriting N "))

summ = 0

for i in range(0,N):
	summ = summ	+ pow(A,i)
	print(pow(A,i))
	print('+')

print('summa - ',summ)