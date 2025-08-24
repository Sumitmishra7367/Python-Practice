# find smallest value in the list
list_2=[11,20,4,50,41,3,88,77,93,85,78,99,44]
small=min(list_2)
print("The smallest value is : ",small)

#second method
list_1=[11,20,4,2,50,41,88,77,93,85,78,99,44]
minimum=sorted(set(list_1))[0]
print("The smallest value is : ",minimum)

#third method
list_3=[11,20,4,2,50,41,88,77,93,85,78,99,44]
smallest_value=list_3[0]
for i in list_3:
    if i<smallest_value:
        smallest_value=i
print("The smallest value is : ",smallest_value)