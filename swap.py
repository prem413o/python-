#t a program that swaps the values of two
#variables

def swap(a,b):
    t=a
    a=b
    b=t
    return a,b

a=int(input("Enter first number: "))
b=int(input("Enter second numbe: "))

result=swap(a,b)
print("the number before swapping is",a,b)
print("the number after swapping is",result)
