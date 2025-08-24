#find vowel count

words = ['apple', 'banana', 'grapes', 'mango']
vowels="aeiouAEIOU"
count=0
for word in words:
    for char in word:
        if char in vowels:
            count+=1
print("the vowel number is : ",count)


words = ['apple', 'banana', 'grapes', 'mango','orange']
vowels='aeiouAEIOU'
count=0
for word in words:
    for char in word:
        if char in vowels:
            count+=1
print("The vowel is : ",count)



