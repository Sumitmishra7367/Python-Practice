from functools import reduce

# Find the Largest Number Formed by Digit

digits=[3,1,4,1,5]
sorted_digits=sorted(digits ,reverse=True)
result=reduce(lambda x,y:x+y ,map(str,sorted_digits))
print("The largest number formed by digit is : ",result)
