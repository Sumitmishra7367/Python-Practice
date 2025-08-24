# extract even and odd list from main list


list_2=[11,22,33,44,55,66,77,88,99,100,101,102,103,110,75,65]
odd_list=[]
even_list=[]
for i in list_2:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("The even list is : ",even_list)
print("The odd list is : ",odd_list)