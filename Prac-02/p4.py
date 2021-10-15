# Program to arrange given three numbers in descending order

a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
c=float(input("Enter third number : "))

if a>b and a>c:
    print(a)
    if b>c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b>a and b>c:
    print(b)
    if a>c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if a>b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
