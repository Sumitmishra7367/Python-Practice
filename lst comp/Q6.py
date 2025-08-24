

list_1=[1,2,3,4,5,6,]
result_list=[x**2 if x%2==0 else x for x in list_1]
print(result_list)


list_2=[1,2,3,4,5,6]
square_odd=[i**2 if i%2!=0 else i for i in list_2]
print(square_odd)


