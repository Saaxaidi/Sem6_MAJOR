n =int(input("Enter the number: "))
temp=n

reverse = 0

while temp!=0:
    ld=temp%10
    reverse=(reverse*10)+ld
    temp//=10

if n==reverse:
    print("true")
else:
    print("false")