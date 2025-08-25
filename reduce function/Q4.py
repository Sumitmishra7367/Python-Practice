from functools import reduce


list_1=["Hello", "Python", "World"]
Result=reduce(lambda x,y:x+y,list_1)
print(Result)
