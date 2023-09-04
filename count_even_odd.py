numbers = 10

even=0
odd=0
for i in range(1,numbers):
    if i%2==0:
        even+=1
    else:
        odd+=1
print (f"no of even no are {even} \nno of odd  no are {odd} ")