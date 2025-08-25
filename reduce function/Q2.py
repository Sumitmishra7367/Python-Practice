from functools import reduce

#sum of all list element

list_1=[2,4,6,8]
result=reduce(lambda x,y :x+y,list_1)
print("Sum : ",result)

#product of list

list_2=[1,2,3,4,5]
re=reduce(lambda x,y:x*y,list_2)
print("product:",re)