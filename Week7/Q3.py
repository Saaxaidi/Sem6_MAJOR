n = int(input("enter the number: "))

def fact(n):
    fact =1

    for i in range(1,n+1):
        fact*=i

    print(f"factorial of {n} is {fact}")

fact(n)