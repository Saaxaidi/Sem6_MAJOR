data = eval(input("Enter list: "))

# Sort the list
data.sort()

is_consecutive = True

for i in range(len(data) - 1):
    if data[i+1] - data[i] != 1:
        is_consecutive = False
        break

print(is_consecutive)