from functools import reduce


# Find Maximum Number

list_1=[12, 45, 2, 67, 34, 89, 23]
result=reduce(lambda x,y:x if x>y else y ,list_1)
print("Maximum : ",result)

list_2=[12, 45, 2, 67, 34, 89, 23]
result=reduce(lambda x,y: x if x<y else y ,list_2 )
print(result)

