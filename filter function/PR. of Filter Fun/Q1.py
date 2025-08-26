# print a even numbers in the list

list_1=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda x:x%2==0,list_1))
print("The even number is : ",result)





# print a Odd numbers in the list

list_2=[11,22,33,44,55,66,77,88]
resul=list(filter(lambda x:x%2!=0,list_2))
print("The odd numbers is : ",resul)