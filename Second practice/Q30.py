# first occurrence of digit in string


str_1="hello54321world"
for i in str_1:
    if i.isdigit():
        print("First digit found of",i)
        break



str_2="hello2521world"
for char in str_2:
    if char.isdigit():
        print("The first digit found of : ",char)
        break
