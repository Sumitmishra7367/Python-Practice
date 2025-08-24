# replace vowels with $
str_1="aditya golu Sumit Mishra "
vowels="aeiouAEIOU"
replace=" "
for char in str_1:
    if char in vowels:
        replace+="$"
    else:
        replace+=char
print("original string ",str_1)
print("replaced string",replace)
