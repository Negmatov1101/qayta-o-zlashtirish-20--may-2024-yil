
A = int(input("kiriting A: "))

flag = True

while A < 0:
	A = int(input("kiriting A: "))

if (A > 99 and A < 1000) and A % 2 != 0:
	pass
else:
	flag = False

print(flag)