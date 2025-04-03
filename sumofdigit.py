def number_of_digit(n):
    if(n>=1 and n<=9):
        return 1
    elif(n==0):
        return 1
    
    smallNumber= int(n/10)
    smallans= number_of_digit(smallNumber)

    ans=1+smallans
    return ans


print(number_of_digit(123))