from functools import reduce

#find minimumm element
nums = [45, 12, 78, 4, 90, 23]
result=reduce(lambda x,y:x if x<y  else y ,nums)
print(result)
