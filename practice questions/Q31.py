#eplace vowels with $

str="Hello World"
vowels="AEIOUaeiou"
result=""
for char in str:
    if char in vowels:
        result+="$"
    else:
        result+=char
print("original string : ",str)
print("after replacing string : ",result)














str_1="Sumit Mishra"
vowels='aeiouAEIOU'
result=""
for i in str_1:
    if i in vowels:
        result+="$"
    else:
        result+=i
print("original string : ",str_1)
print("after replacing string : ",result)



















str_2="Aditya Mishra"
vowels="aeiouAEIOU"
result=""
for a in str_2:
    if a in vowels:
        result+="$"
    else:
        result+=a
print("Original string : ",str_2)
print("After repacing string : ",result)