# ##Q13. find count of each data type

# mixed_list = [10, 3.14, 'hello', True, None, [1, 2], {'a': 1}, (5, 6), 20, False, 'world']
# type_count={}
# for item in mixed_list:
#     t=type(item).__name__
#     if t in type_count:
#         type_count[t]+=1
#     else:
#         type_count[t]=1
# print(type_count)


#another method

mixed_list = [10, 3.14, 'hello', True, [1, 2], {'a': 1}, (5, 6), 20, False, 'world']
count_int=0
count_float=0
count_str=0
count_bool=0
count_dict=0
count_list=0
count_tuple=0

for i in mixed_list:
    if type(i) ==int:
        count_int+=1
    elif type(i) ==float:
        count_float+=1
    elif type(i) == str:
        count_str+=1
    elif type(i) ==bool:
        count_bool+=1
    elif  type(i) == dict:
        count_dict+=1
    elif type(i) ==list:
        count_list+=1
    elif type(i)== tuple:
        count_tuple+=1
print("The int number is : ",count_int)
print("The float number is : ",count_float)
print("The str number is : ",count_str)
print("The bool number is : ",count_bool)
print("The dict number is : ",count_dict)
print("The list number is : ",count_list)
print("The tuple number is : ",count_tuple)














mixed_list = [10, 3.14, 'hello', True, [1, 2], {'a': 1}, (5, 6), 20, False, 'world']
type_count={}
for i in mixed_list:
    t=type(i).__name__
    if t in type_count:
        type_count[t]+=1
    else:
        type_count[t]=1
    print(type_count)