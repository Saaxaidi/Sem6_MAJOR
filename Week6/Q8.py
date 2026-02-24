data = eval(input("Enter a list: "))

total = 0

for item in data:
    if isinstance(item, int):
        total += item

print("Sum of integers:", total)