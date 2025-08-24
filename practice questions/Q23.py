#print each data type of different element in list


my_list = [10, "apple", 3.14, True, [1, 2, 3], (5, 6)]

for item in my_list:
    print(item, "=>", type(item).__name__)






list_1= [10, "apple", 3.14, True, [1, 2, 3], (5, 6)]
for i in list_1:
    print(i,"=>",type(i).__name__)


list_3= [10, "apple", 3.14, True, [1, 2, 3], (5, 6)]
for num in list_3:
    print(num, "=>",type(num).__name__)
    





list_2= [10, "apple", 3.14, True, [1, 2, 3], (5, 6)]
for data in list_2:
    print(data,"=>" ,type(data).__name__)
