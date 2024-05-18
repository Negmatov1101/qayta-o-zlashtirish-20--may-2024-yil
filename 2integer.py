
A = int(input("kiriting А: "))

while A < 999:
	print(A)
	A = int(input("kiriting А: "))

sotni, des = divmod(A,100)

des, ed = divmod(des,10)

print('Chislo', A)
print(sotni)