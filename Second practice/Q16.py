# find greatest value in list
list_2=[11,20,4,50,41,88,77,93,85,78,99,44]
maximum=max(list_2)
print("The greatest value is : ",maximum)


#Second method
list_3=[11,20,4,50,41,88,77,93,85,78,99,44]
great=sorted(set(list_3))[-1]
print("The greatest value is : ",great)


#third method
list_1=[11,20,4,50,41,88,77,93,85,78,110,44]
greatest_value=list_1[0]
for i in list_1:
    if i > greatest_value:
        greatest_value=i
print("The greatest value is : ",greatest_value)