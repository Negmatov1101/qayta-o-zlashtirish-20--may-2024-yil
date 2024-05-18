
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

while A < C or B < C:
	A = float(input("A = "))
	B = float(input("B = "))

buf = B

cnt = 0

while A > C:
	while B > C:
		cnt += 1
		B = B - C

	A = A - C
	cnt += 1
	B = buf

print(cnt)