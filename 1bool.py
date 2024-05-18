
A = int(input("raqam kiriting A: "))

B = int(input("raqam kiriting B: "))

if (A % 2 != 0 and B % 2 == 0) or (A % 2 == 0 and B % 2 != 0):
	print(True)
else:
	print(False)