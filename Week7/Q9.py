# Input list
nums = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(nums)

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            # Swap
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

# Second largest element
if n < 2:
    print("List must have at least 2 elements")
else:
    print("Sorted List:", nums)
    print("Second Largest Number:", nums[-2])