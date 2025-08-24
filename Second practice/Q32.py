# replace all numbers in string with special character 
str_1="sumit5425mis544h45ra2"
replace=""
for num in str_1:
    if num.isdigit():
        replace+="#"
    else:
        replace+=num
print("The original string : ",str_1)
print("The replaced string : ",replace)