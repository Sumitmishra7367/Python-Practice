# first occurrence of digit in string
str_1="hello1234world"
for char in str_1:
    if char.isdigit():
        print("first digit found",char)
        break

    