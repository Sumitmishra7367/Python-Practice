# Words को उनकी length के आधार पर sort करो।
# फिर reverse alphabetical order में sort करो।

words = ["python", "machine", "ai", "deep", "learning"]
sorted_list=sorted(set(words))      #ye alphabets ke hisab se sort kar raha hai
print(sorted_list)
words.sort(reverse=True)
print(words)               # ye alphabets ke hisab se sort kar raha hai mtlb abcde ke hisab se 



word = ["python", "machine", "ai", "deep", "learning"]
word.sort(key=len)
print(word)


word.sort(key=len,reverse=True)
print(word)