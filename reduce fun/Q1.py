
from functools import reduce


#sum of all list element

list_1=[1,2,3,4,5]                                      
result=reduce(lambda x,y:x+y,list_1)
print(result)

#print of each string to  one string

list_2=["I","am","a","boy"]
result=reduce(lambda x,y:x+" "+y,list_2)
print(result)


list_3=["Hello","My","name","is","Sumit","Mishra"]
res=reduce(lambda x,y:x+" "+y,list_3)
print(res)



