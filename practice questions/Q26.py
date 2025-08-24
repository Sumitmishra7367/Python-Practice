#print length of even numbers and odd numbers to given list 

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,]
even_count=0
odd_count=0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("This is the even numbers : ",even_count)
print("This is the odd numbers",odd_count)


#average of the list


list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
total=0
average=0
for i in list_1:
    total+=i
    average=total/15
print("Average=" ,average)


