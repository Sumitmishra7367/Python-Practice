# find even elements in a list
list_2=[11,22,33,44,55,66,77,88,99,100,101,102,103,110]
even_list=[]
for i in list_2:
    if i%2==0:
        even_list.append(i)
print("The even list is ",even_list)