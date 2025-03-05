# Given a list of numbers, find the sum and average)

num=[1,14,25,32,10,45,46,78,98,100]

sum=0
i=0
while i<len(num):
    sum= sum + num[i]
    i+=1

print("the sum of number is",sum)

average=sum/len(num)
print("the average of this list is",average)
