
x = int(input("Kiriting x: "))

while x > 999 and x < 1:
	x = int(input("kiriting x: "))

param1 = ''
param2 = ''

if x < 10:
	param1 = 'bir xonali'
elif x < 100:
	param1 = 'Ikki xonali'
elif x < 1000:
	param1 = 'Uch xonali'

if x % 2 == 0:
	param2 = 'juft  '
else:
	param2 = 'toq '

print(param1,param2)