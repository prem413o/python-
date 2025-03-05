#(Implement a program that swaps the values of two variable
a=int(input("Enter your first number: "))
b=int(input("Enter second number: "))

def swap(a,b):
    t=a
    a=b
    b=t
    return a,b

result=swap(a,b)

print("the number before swapping is",a,b)
print("the number after swapping is",result)