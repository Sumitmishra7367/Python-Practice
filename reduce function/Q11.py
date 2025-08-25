from functools import reduce

# Find the Second Largest Element using reduce

nums = [12, 45, 7, 89, 34, 67]
sorted_list=sorted(nums)
result=reduce(lambda x,y : x if x>y else y ,sorted_list)
print(result)
