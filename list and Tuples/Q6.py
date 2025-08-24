#find even number in the lists
list_1=[10,11,12,1,2,3,22,33,44,55,66,77,88,99,100]
even_number=[]
odd_number=[]
for num in list_1:
    if num%2==0:
        even_number.append(num)
    else:
        odd_number.append(num)
print("The even number is : ",even_number)
print("The odd number is : ",odd_number)
