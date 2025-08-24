#find vowel count


text = "Hello World! Welcome to Python."
vowel="aeiouAEIOU"
count=0
for i in text:
    if i in vowel:
        count+=1
print("the vowel number is : ",count)




words = ['apple', 'banana', 'grapes', 'mango']
vowels="aeiouAEIOU"
count=0
for word in words:
    for char in word:
        if char in vowels:
            count+=1
print("The vowel number is :  ",count)













words = ['apple', 'banana', 'grapes', 'mango']
vowels="aeoiouAEIOU"
count=0
for word in words:
    for char in word:
        if char in vowels:
            count+=1
print("the vowel number is : ",count)