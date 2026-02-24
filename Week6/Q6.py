import math
s1 =int(input("Enter the size of s1: "))
s2 =int(input("Enter the size of s2: "))
s3 =int(input("Enter the size of s3: "))

# Check if valid triangle
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    s = (s1+s2+s3)/2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    print("area of triange : ",area)

    if s1 == s2 == s3:
        print("Triangle is Equilateral")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Triangle is Isosceles")
    else:
        print("Triangle is Scalene")
else:
    print("invalid triangle")
