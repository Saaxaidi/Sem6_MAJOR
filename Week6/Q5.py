month = int(input("Enter the months number(1-12): "))
year =int(input("Enter the year : "))

days =[31,29,28,31,30,31,30,31,31,30,31,30,31]

if 1 <= month <= 12:
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print("Number of days:", 29)
    else:
        print("Number of days:", days[month - 1])
else:
    print("Invalid month")