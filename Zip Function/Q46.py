from functools import reduce


list_1=["Apple","orange","data","Science"]
result=[]
for i in list_1:
    if len(i)>5:
        result.append(i)
print(result)