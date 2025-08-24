#replace all numbers in string with special character 
string="hello1234world567"
result=""
for num in string:
    if num.isdigit():
        result+="#"
    else:
        result+=num
print("orginal string : ",string)
print("after replacing string : ",result)








str_1="hello1W2o3r4ld5sumit6m7i8s9h"
result=""
for char in str_1:
    if char.isdigit():
        result+="#"
    else:
        result+=char
print("orginal string : ",str_1)
print("after replacing string : ",result)







