num=[34,2,7,38,88,2,89]
max=num[0]
min=num[0]

i=0
while i<len(num):
    if(num[i]>max):
        max=num[i]
    elif(num[i]<min):
        min=num[i]
i+=1

print("the maximum number of list is",max)
print("the minimum in a list is",min)
