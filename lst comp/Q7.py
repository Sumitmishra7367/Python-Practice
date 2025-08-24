#print the second largest element in the list 
list_1=[122,11,99,66,33,22,55,44,88,]
secoond_lar_elem=sorted(set(list_1))[-2]
print("The second largest element is : ",secoond_lar_elem)


list_2=[122,11,99,66,33,22,55,44,88,]
unique_list=list(set(list_2))
unique_list.sort()
print("The second largest elemnt is ",unique_list[-2])
