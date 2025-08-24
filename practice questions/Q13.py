#Q13. find count of each data type

# mixed_list = [10, 3.14, 'hello', True, None, [1, 2], {'a': 1}, (5, 6), 20, False, 'world']
# type_count={}
# for item in mixed_list:
#     t = type(item).__name__
#     if t in type_count:
#         type_count[t]+=1
#     else:
#         type_count[t]=1
# print(type_count)






# data = [10, 3.5, 'hello', True, None, [1, 2], {'a': 1}, (1, 2), 'world', False, 99]
# type_count={}
# for item in data:
#     t=type(item).__name__
#     if t in type_count:
#         type_count[t]+=1
#     else:
#         type_count[t]=1
# print(type_count)







# mixed_list = [10, 3.14, 'hello', True, None, [1, 2], {'a': 1}, (5, 6), 20, False, 'world']
# type_count={}
# for item in mixed_list:
#     t=type(item).__name__
#     if t in type_count:
#         type_count[t]+=1
#     else:
#         type_count[t]=1
# print(type_count)



















# data = [10, 3.5, 'hello', True, None, [1, 2], {'a': 1}, (1, 2), 'world', False, 99]

# type_count={}
# for i in data:
#     t=type(item).__name__
#     if t in data:
#         type_count[t]=+1
#     else:
#         type_count[t]=1
# print(type_count)








data = [10, 3.5, 'hello', True, None, [1, 2], {'a': 1}, (1, 2), 'world', False, 99]
type_count={}
for item in data:
    t=type(item).__name__
    if t in type_count:
        type_count[t]+=1
    else:
        type_count[t]=1
print(type_count)


list_1=[1,2.5,2.67,"sumit",True]
count_int=0
count_float=0
count_str=0
count_bol=0
count_str=0
for i in list_1:
    if type (i) ==int:
        count_int+=1
    elif type (i) ==str:
        count_str+=1
    elif type (i) ==bool:
        count_bol+=1
    elif type(i) ==float:
        count_float+=1
print(count_int)
print(count_float)

print(count_bol)
