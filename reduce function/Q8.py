from functools import reduce

# Multiply All Odd Numbers in a List

nums = [2, 3, 5, 6, 7, 8, 9]
odd_number=list(filter(lambda x:x%2!=0,nums) )
result=reduce(lambda x,y:x*y,odd_number)
print("The product of all odd number is : ",result)  
