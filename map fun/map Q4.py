#sum of two list

list_1=[1,5,2]
list_2=[3,5,8]
result=list(map(lambda x,y:x+y,list_1,list_2))
print(result)


#sum of three list

num_1=[5,8,9]
num_2=[6,4,2]
num_3=[1,3,7]
result=list(map(lambda x,y,z:x+y+z,num_1,num_2,num_3))
print(result)
