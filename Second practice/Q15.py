# find even number in the lists
list_1=[11,20,12,31,22,25,42,55,66,44,10,28,14,26,21]
even_list=[]
for num in list_1:
    if num%2==0:
        even_list.append(num)
print("The even list is  : ",even_list)