n = int(input("Enter the number: "))
temp1=n
temp2=n

# count the digit ->
count=0
while(temp1!=0):
    ld =temp1%10
    count+=1
    temp1//=10

#check the armstring number->
tsum =0
while(temp2!=0):
    ld =temp2%10
    tsum=tsum+pow(ld,count)
    temp2//=10

if n==tsum:
    print(f"{n} is the armstrong number")
else:
    print(f"{n} is not a armstrong number")
