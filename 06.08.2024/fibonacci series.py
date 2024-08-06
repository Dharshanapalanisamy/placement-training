n = 10
n1 = 0
n2 = 1
number = n2 
count = 1
while count <= n:
	print(number, end=" ")
	count += 1
	n1, n2 = n2,number
	number = n1 + n2
print()
