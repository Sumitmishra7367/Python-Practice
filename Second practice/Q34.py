#print the count of vowel and consonant in string

str_1="hello my name is sumit mishra "
vowels="AEIOUaeiou"
vowels_count=0
consonant_count=0
for item in str_1:
    if item.isalpha(): #sirf alphabets ko ginne ke liye
        if item in vowels:
             vowels_count+=1
        else:
            consonant_count+=1

print("The count of all vowels are : ",vowels_count)
print("The count of all constant are : ",consonant_count)