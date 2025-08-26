from functools import reduce

#Sum of Cubes (reduce)


list_1=[1,2,3,4,5]
result=reduce(lambda x,y:x+y**3,list_1)
print(result)