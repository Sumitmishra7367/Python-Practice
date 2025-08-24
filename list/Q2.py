# Q11. find length of list

list_1=[1,2,3,4,5,6,7,8,9,10,22,33,44]
length=len(list_1)
print("The length of list is : " ,length) 


list_2=[1,2,3,4,5,6,7,8,9,10,22,33,44]
count=0
for i in list_2:
    if i >0:
        count+=1
    else:
        count=1
print("The lenght of list is : ",count)
