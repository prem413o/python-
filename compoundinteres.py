P=int(input("Enter your  principal amount: "))
T=int(input("Enter your time period: "))
Rate=int(input("Enter your rate of interest: "))

amount=P*(pow(1+Rate/100,T))
Compund_Interest=amount-P

print("the Compound interest is ",Compund_Interest)