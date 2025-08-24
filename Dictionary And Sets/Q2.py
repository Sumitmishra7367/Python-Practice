#counnt vowel

text = "programming"

vowels="AEIOUaeiou"
count=0
for i in text:
    if i in vowels:
        count+=1
print("The count of all vowels are : ",count)