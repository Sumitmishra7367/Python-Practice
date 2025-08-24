# print sum of integers type in list
list_1=[22,10.2,50,11,True,"Sumit",41,36.1,63]
int_sum=0
for i in list_1:
    if type(i) == int:
        int_sum+=i
print("The sum of all integers : ",int_sum)




data = [10, 3.5, 'hello', True, None, [1, 2], 20, 'world', False, 15,11,31]
int_total=0
for num in data:
    if type(num)==int:
        int_total+=num

print("The sum of all integers : ",int_total)

