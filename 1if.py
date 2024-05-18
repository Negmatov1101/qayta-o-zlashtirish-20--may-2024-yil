
x = float(input("kiriting x: "))
fx = 0

if x < 0:
	fx = 0
elif (x >= 0 and x < 1) or (x >= 2 and x < 3):
	fx = 1
elif (x >= 1 and x < 2) or (x >= 3 and x < 4):
	fx = -1

print(fx)