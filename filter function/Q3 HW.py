# print upper case of each string

words=["abCdE","eFgHi","GjK"]

result=["".join(filter(lambda x : x.isupper(),w)) for w in words]
print(result)






list_2=["abCdE","eFgHi","GjK"]
resu=["".join(filter(lambda x:x.isupper(),z)) for z in list_2]
print(resu)





list_1=["abCdE","eFgHi","GjK"]
r=["".join(filter(lambda y:y.isupper(),x)) for x in list_1 ]
print(r)



list_3=["abCdE","eFgHi","GjK"]
re=["".join(filter(lambda x:x.isupper(),w)) for w in list_3]
print(re)