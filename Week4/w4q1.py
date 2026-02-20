# Function to compute the average marks
def compute_average(marks):
    if len(marks) != 5:
        return "Please enter exactly five marks."
    return sum(marks) / 5


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Average of marks
marks = [-10, 0, 20, 30, 40]
average = compute_average(marks)
print("Average =", average)

# Temperature conversion
temperature_c = 36.5
temperature_f = celsius_to_fahrenheit(temperature_c)
print("Temperature in Fahrenheit =", temperature_f, "°F")

#Perimeter of notice board
length = 5
width = 3
perimeter = rectangle_perimeter(length, width)
print("Perimeter of notice board =", perimeter)
