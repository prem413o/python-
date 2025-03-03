num=[12,25,68,41,10]

max=num[0]
min=num[0]

i=0
while i<len(num):
    if(num[i]>max):
        max=num[i]
    elif(num[i]<min):
        min=num[i]
    i+=1

print("the maximum value is ",max)
print("the min value is ",min)
