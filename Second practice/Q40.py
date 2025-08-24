# remove duplicate elements in a list

list_1=[1,1,2,2,3,3,4,4,5,5,6,6]
unique_list=[]
for num in list_1:
    if num not in unique_list:
        unique_list.append(num)
print("lis without duplicate is : ",unique_list)






list_2=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,]
unique_list=[]
for i in list_2:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
