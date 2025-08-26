from functools import reduce

# Lambda + reduce:
# एक list दी है: [2, 4, 6, 8, 10]
# Reduce function से इनका sum निकालो।
# Reduce function से इनका multiplication निकालो।

list_1=[2,4,6,8]
sum_of_list=reduce(lambda x,y:x+y,list_1)
multy_of_list=reduce(lambda x,y:x*y,list_1)
print("The sum of element is : ",sum_of_list)
print("The multiplication of list is : ",multy_of_list)
