# find count of each data type
mixed_list=[True,14,15.23,False,"Sumit",(1,2)]
type_count={}
for item in mixed_list:
    t=type(item).__name__
    if t in type_count:
        type_count[t]+=1
    else:
        type_count[t]=1
print(type_count)




list_4=[True,14,15.23,False,"Sumit",(1,2)]
type_count={}
for i in list_4:
    t=type(i).__name__
    if t in type_count:
        type_count[t]+=1
    else:
        type_count[t]=1
print(type_count)














list_1=[True,14,15.23,False,"Sumit",(1,2)]
type_count={}
for i in list_1:
    t=type(i).__name__
    if t in type_count:
        type_count[t]+=1
    else:
        type_count[t]=1
print(type_count)








list_2=[True,14,15.23,False,"Sumit",(1,2)]
type_count={}
for itm in list_2:
    t=type(itm).__name__
    if t in type_count:
        type_count[t]+=1
    else:
        type_count[t]=1
print(type_count)



