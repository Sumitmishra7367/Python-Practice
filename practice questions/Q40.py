#remove duplicate elements in a list
list_1=[1,1,2,2,3,3,4,4,5,5,6,6]
unique_list=[]
for num in list_1:
    if num not in unique_list:
        unique_list.append(num)
print("List withot list is :",unique_list)







list_2=[11,11,12,12,13,13,14,14,15,15,16,16,17,17]
unique_list=[]
for i in list_2:
    if i not in unique_list:
        unique_list.append(i)
print("List withou duplicate is : ",unique_list)
