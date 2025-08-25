from functools import reduce 

# Check if All Elements Are Equal
nums=[10,10,10,10]
resul=reduce(lambda x,y:x if x==y else False,nums)
if resul is False:
    print("All element is are not equal")
else:
    print("All elment is are equal")
















numbers=[20,20,20,20,20]
result=reduce(lambda x,y:x if x==y else False ,numbers)
if result is False:
    print("All elemt is are not equal")
else:
    print("All element is equal")
