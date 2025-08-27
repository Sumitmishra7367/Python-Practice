# Missing numbers problem:
# nums = [1, 2, 4, 6, 7, 10]
# Output: missing numbers (3, 5, 8, 9)।

nums = [1, 2, 4, 6, 7, 10]


min_num=min(nums)
max_num=max(nums)
missing_number=[x for x in range(min_num,max_num+1) if x not in nums]
print(missing_number)

