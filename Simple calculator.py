#SIMPLE CALCULATOR FOR ARITHMETIC OPERATIONS
def add(a,b):
    s=a+b
    return s
def sub(a,b):
    t=a-b
    return t
def mult(a,b):
    u=a*b
    return u
def div(a,b):
    v=a/b
    return v
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
n=int(input("Enter the number corresponding to your required operation:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if n==1:
    print("Sum is",add(a,b))
elif n==2:
    print("Difference is",sub(a,b))
elif n==3:
    print("Product is",mult(a,b))
else:
    print("Division answer is:",div(a,b))
    
