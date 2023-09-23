
def get_reverse(string):
    for i in string:
        reverse = string[::-1]
    return reverse
string = input("Enter any string")
res = get_reverse(string)
print(res)