t1 = float(input("Enter the temp for probes 1:  "))
t2 = float(input("Enter the temp for probes 2:  "))
t3 = float(input("Enter the temp for probes 3:  "))

if(t1<t2) and (t1<t3):
    print(t1 ," is the lowest temperature")
elif(t2<t1) and (t2<t1):
    print(t2, " is the lowest temperature")
else:
    print(t3," is the lowest temperature")