a =int(input("Enter the number : "))
b =int(input("Enter the number : "))

def find_signal_sync(a, b):
    if b==0:
        return a
    else:
        return find_signal_sync(b, a%b)
    
result= find_signal_sync(a,b)

print(result)