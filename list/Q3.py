# Q3.find even count in list

list_1=[22,23,24,11,10,44,45,12,78,96,45,42,52,51]
even_count=0
odd_count=0
for i in list_1:
    if i %2==0:
        even_count+=1
    else:
        odd_count+=1


print("the even number is : ",even_count)
print("the odd number is : ",odd_count)
