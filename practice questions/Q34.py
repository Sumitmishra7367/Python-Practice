#print the count of vowel and consonant in string
string="Hello World"
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for char in string:
    if char.isalpha():
        if char in vowels:
             vowel_count+=1
        
        else:
            consonant_count+=1
print("the vowels are : ",vowel_count)
print ("the constant are  : ",consonant_count)


string = "Hello World"
vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0
for char in string:
    if char.isalpha():  # सिर्फ alphabets को check करेंगे
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
