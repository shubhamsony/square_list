def sum_of_squares():
    num = input("Enter a list of numbers separated by spaces: ").split()
    total = 0
    for n in num:
        total += int(n) ** 2
    return total
result = sum_of_squares()
print(result)