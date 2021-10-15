# Program to make a simple calculator

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

num1=float(input("Enter a number : "))
op=input("Enter operator : ")
num2=float(input("Enter a number : "))

if op == '+':
    print(add(num1,num2))
elif op == '-':
    print(subtract(num1,num2))
elif op == '*':
    print(multiply(num1,num2))
elif op == '/':
    print(divide(num1,num2))
else:
    print("Invalid operator")
        
