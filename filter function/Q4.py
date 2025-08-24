#extract those city with less thann 2m population

city=[("Mumbai",1.5),("Delhi",1),("Mohali",2.5)]

result=list(filter(lambda x:x[1]<2,city))

result_1=list(map(lambda x:x[0],result))
print(result_1)


#without lambda fun.

def miilions(x):
    return x[1]<2
xity=[("Mumbai",1.5),("Delhi",1),("Mohali",2.5)]
res=list(filter(miilions,xity))
print(res)
