import math
#a part
def largest_number(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
            return b
    else:
        return c
        
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
z=int(input("enter the third number: "))
print("largest number:",largest_number(x,y,z))

#b part
def volume_cylinder(r,h):
    return math.pi *r*r*h

def volume_cube(a):
    return a*a*a

def volume_rectangular_box(l,w,h):
    return l*w*h

print("choose the shape to find volume")
print("1 -> cylinder")
print("2 -> cube")
print("3 -> rectangular box")

choice =int(input("enter your choice: "))

if choice == 1:
    r =int(input("Enter the radius: "))
    h= int(input("enter the height: "))
    print("volume of cylinder: ",volume_cylinder(r,h))
elif choice == 2:
    a=int(input("enter the side of the cube: "))
    print("volume of cube: ",volume_cube(a))
elif choice == 3:
    l =int(input("enter the length of a rectangular box: "))
    w =int(input("enter the width of a rectangular box: "))
    h = int(input("enter the height of a rectangular box:"))
    print("volume of rectangular box: ",volume_rectangular_box(l,w,h))
    volume_rectangular_box(l,w,h)
else:
    print("invalid choice ")
    
#c part
def rectangle_area(l,w):
    return l*w

l=int(input("enter the length: "))
w=int(input("enter the width: "))
print("area: ",rectangle_area(l,w))

#d part
def circumference_of_circle(r):
  return 2*math.pi*r

r=int(input("enter the radius: "))
print("circumference: ",circumference_of_circle(r))

#e part
def swap(a,b):
 temp =a;a=b;b=temp
 return a,b

x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
x,y =swap(x,y)
print("after swapping:")
print("first number: ",x)
print("second number: ",y)

#f part
def Cal_distance(x1,y1,x2,y2):
    return math.dist((x1,y1),(x2,y2))

x1= float(input("enter x1: "))
y1= float(input("enter y1: "))
x2= float(input("enter x2: "))
y2= float(input("enter y2: "))
print("distance between two points: ",Cal_distance(x1,y1,x2,y2))