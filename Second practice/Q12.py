# find even count in list
list_1=[22,11,55,42,21,12,64,36,52,10,13]
even_count=0
for num in list_1:
    if num%2==0:
        even_count+=1
print("The count of all even number is : ",even_count)




# find odd count in list
list_2=[22,11,55,42,21,12,64,36,52,10,13,4,31,15,18]
odd_count=0
for i in list_2:
    if i %2!=0:
        odd_count+=1
print("The count of all odd number is : ",odd_count)