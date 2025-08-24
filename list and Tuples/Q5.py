# print sum of integers type in list 
data = [10, 3.5, 'hello', True, None, [1, 2], 20, 'world', False, 15,5.6,4.5,3.3,2.5]
total=0
for i in data:
    if type(i)==int:
        total+=i
print("the sum of integers: ",total)


numbers= [10, 3.5, 'hello', True, None, [1, 2], 20, 'world', False, 15,5.6,4.5,3.3,2.5]
total=0
for item in numbers:
    if type(item)==float:
        total+=item
print("The sum of float number is : ",total)
