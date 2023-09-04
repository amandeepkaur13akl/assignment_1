no=50
num1 = 0
num2 = 1
next_number = num1

while next_number <= no:
	print(next_number, end=" \n")
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()
