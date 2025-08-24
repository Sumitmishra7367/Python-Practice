#find even number in the lists

list_1=[10,11,12,1,2,3,22,33,44,55,66,77,88,99,100]
even_number=[]
for i in list_1:
    if i %2==0:
       even_number.append(i)
print("The even number is : ",even_number)







list_2=[10,11,12,1,2,3,22,33,44,55,66,77,88,99,100]
even_number=[]
for i in list_2:
    if i%2==0:
        even_number.append(i)
print("The even number is: ",even_number)










list_5=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
even_number=[]
odd_number=[]
for i in list_5:
    if i %2==0:
        even_number.append(i)
    else:
        odd_number.append(i)
print("the even number is : ", even_number)
print("the odd number  is : ",odd_number)
