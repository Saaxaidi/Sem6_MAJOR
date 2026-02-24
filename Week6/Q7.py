# Input two numbers
r1 = int(input("Enter starting ID (r1): "))
r2 = int(input("Enter ending ID (r2): "))

# Check condition
if r1 < r2:
    id_list = list(range(r1, r2 + 1))   # r2 + 1 to make it inclusive
    print("List of IDs:", id_list)
else:
    print("Invalid input! r1 should be less than r2.")