size1 = int(input("Enter the size of 1st list: "))
size2 = int(input("Enter the size of 2nd list: "))

list1 = []
list2 = []

# Input for 1st list
for i in range(size1):
    el = int(input("Enter the element for 1st list: "))
    list1.append(el)

print("First List:", list1)

# Input for 2nd list
for i in range(size2):
    el = int(input("Enter the element for 2nd list: "))
    list2.append(el)

print("First List:", list1)

list3 = list1+list2
sorted(list3)

print("Sorted list: ",list3)
