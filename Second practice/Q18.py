# increment each element of list by 5
list_1=[15,25,35,45,55,65,75,85,95,100]
incrmented_list=[]
for num in list_1:
    if type(num)==int:
        incrmented_list.append(num+5)
print("The incremented list is : ",incrmented_list)



list_2=[15,25,35,45,55,65,75,85,95,100]
updated_list=[]
for item in list_1:
    updated_list.append(item+5)
print("The incremented list is : ",updated_list)