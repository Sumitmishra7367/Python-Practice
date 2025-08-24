#remove all non-alphabetic characters from a string
text = "Hello World! @2025"
result="".join(char for char in text if char.isalpha())
print(result)


str_1="sumit#@#mishra4256"
result="".join(char for char in str_1 if char.isalpha())
print(result)
