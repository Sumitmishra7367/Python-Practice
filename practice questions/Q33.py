#replace all special characters in string with spaces
str_1="Hell$#@oWor##$ld"
result=""
for char in str_1:
    if not char.isalnum():
        result+=" "
    else:
        result+=char
print("original string : ",str_1)
print("after replacing string : ",result)

















str="sumit1234##$$#$#Mis343hra"
result=""
for i in str:
    if not i.isalnum():
        result+=" "
    else:
        result+=i
print("original string : ",str)
print("after replacing string : ",result)