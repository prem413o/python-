# Write a program to check if a number is prime

n=int(input("Enter your numer: "))
isprime=1

if(n<1):
    print("no prime number exist.")

i=2
while i*i<=n:
    if(n%i==0):
        isprime=0
        break
    i+=1

if(isprime):
    print("the number is prime")
else:
    print("the number is not prime")

