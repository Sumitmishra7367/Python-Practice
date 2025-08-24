# remove all non-alphabetic characters from a string
str_1="hello12312!@!#@!world"
remove="".join(char for char in str_1 if char.isalpha())
print(remove)



str_2="sumit012312!@!#@!mishra"
result="".join(item for item in str_2 if item.isalpha())
print(result)
