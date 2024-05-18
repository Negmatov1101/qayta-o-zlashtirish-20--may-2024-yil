
A = int(input("Kiriting А: "))

while A > 99 or A < 10:
	print(A)
	A = int(input("Kiriting А: "))

a,b = divmod(A,10)

print('unlik - ',a)
print('birlik - ',b)
