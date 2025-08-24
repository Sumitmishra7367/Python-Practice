# find vowel count
str_1="sumit mishra living in mohali"
vowels="AEIOUaeiou"
vowel_count=0
for i in str_1:
    if i in vowels:
        vowel_count+=1
print("The count of all vowels are : ",vowel_count)



words = ['apple', 'banana', 'grapes', 'mango']
vowel="AEIOUaeiou"
count=0
for word in words:
    for char in word:
        if char in vowel:
            count+=1
print("The count of all vowels are : ",count)