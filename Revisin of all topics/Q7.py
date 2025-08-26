# Q1. Square & Filter Evens

List_1= [1,2,3,4,5,6,7,8,9,10]
square=list(map(lambda x :x**2 ,List_1))
print(square)
result=list(filter(lambda x:x%2==0,square))
print(result)