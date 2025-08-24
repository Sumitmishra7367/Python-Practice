# Har word ka frequency dictionary me store karna ha


sentence = "machine learning is fun and machine learning is powerful"
word_count={}
words=sentence.split()
for item in words:
    if item in word_count:
        word_count[item]+=1
    else:
        word_count[item]=1
print(word_count)



