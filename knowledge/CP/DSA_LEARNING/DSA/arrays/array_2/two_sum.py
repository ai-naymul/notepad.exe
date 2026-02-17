target = 60
numbers = [10, 20, 30, 40]

def two_sum(numbers):
    for i in numbers:
        for j in numbers:
            if i+j == target:
                print("Pair Found")
                pair = (i,j)
                return pair
    else:
        print("pair not found")
        return None
result = two_sum(numbers=numbers)
print(result)