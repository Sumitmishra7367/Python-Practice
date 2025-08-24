# Q12.find even count in list


list_1=[22,23,24,11,10,44,45,12,78,96,45,42,52,51]
count_even=0
count_odd=0
for i in list_1:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("This is the even number :",count_even)
print("this is the odd number : ",count_odd)

list_2=[1,2,3,4,5,6,7,8,9,10,11]
count_odd=0
count_even=0
for i in list_2:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("This is the even number",count_even)
print("This is the odd number",count_odd)
