#print length of a string using function without using function

str_1="Hello world"
upper_count=0
lower_count=0
for i in str_1:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
print("Uppercase letter : ",upper_count)
print("lowercase letter : ",lower_count)










str_2="Sumit Mishra"
upper_count=0
lower_count=0
for char in str_2:
    if char.isupper():
        upper_count+=1
    elif char.islower():
        lower_count+=1
print("Uppercase letter : ",upper_count)
print("lowercase letter : ",lower_count)




