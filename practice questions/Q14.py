# Q14. print sum of integers type in list 

data = [10, 3.5, 'hello', True, None, [1, 2], 20, 'world', False, 15]
total=0
for item in data:
    if type(item)==int:
        total+= item
print("sum of integers ",total)








list_1=[11, 3.5, 'hello', True,31, None, [1, 2], 20, 'world', False, 25,35,55]
total=0
for i in list_1:
    if type(i) ==int:
        total+=i
print("The sum of integers :",total)
