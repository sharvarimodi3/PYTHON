lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = input("Enter value: ")
    if value.isdigit():
        lst.append(int(value))
    else:
        lst.append(value)
numbers = []
names = []
for x in lst:
    if isinstance(x, int):
        numbers.append(x)
    else:
        names.append(x)
print("Numbers:", numbers)
print("Maximum number:", max(numbers))
names.sort(reverse=True)
print("Names in descending order:", names)