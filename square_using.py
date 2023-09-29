lst = int(input("Enter the size of list:"))
new_lst = []
for i in range(lst):
    elements = int(input("Enter the elements of list:"))
    new_lst.append(elements)
print(f"lst: {new_lst}")
def get_square(new_lst):
    return new_lst * new_lst
result = list(map(get_square,new_lst))
print(result)
