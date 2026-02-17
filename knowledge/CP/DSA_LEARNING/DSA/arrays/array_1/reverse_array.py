a = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    a.append(input(f"Enter the {i}th element: "))
print(f"The original array is: {a}")
result = a[::-1]
print(result)