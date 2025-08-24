#print empty string not empty string

item=["Apple","Orange","  "]
empty="  "
result=list(filter(lambda x:x in empty,item))
print(result)



list_1=["Apple","Orange"," "]
r=list(filter(lambda x:x!=" ",list_1))
print(r)
