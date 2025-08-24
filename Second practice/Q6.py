# print first letter or word is vowel or not
sentence=input("Enter the word : ")
first_char=sentence.strip()[0]
if first_char in "aeiouAEIOU":
    print("The first character is vowel")
else:
    print("The first character is not vowel")







sentence_1=input("Enter the word : ")
first_character=sentence_1.strip()[0]
if first_character in "AEIOUaeiou":
    print("The First letter is vowel")
else:
    print("The first letter is not vowel")





sentence_2=input("Enter the sentence : ")
first_chr=sentence_2.strip()[0]
if first_chr in "AEIOUaeiou":
    print("The first character is vowel")
else:
    print("The First character is not vowel")














sentence_3=input("Enter the sentence : ")
for char in sentence_3:
    first_letter=sentence_3.strip()[0]
    if first_letter in "AEIOUaeiou":
        print("the first letter is vowel")

    else:
        print("The first letter is not vowel")