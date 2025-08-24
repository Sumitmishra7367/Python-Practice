# Tumhe ek dictionary banana hai jisme har word ki frequency (count) store ho.

sentence = "python is easy and python is powerful"
word_count={}
words=sentence.split()
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)




text = "python is fun and python is powerful and python is easy"
count={}
alpha=text.split()
for i in alpha:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)














# same logic but question differant

sentenc= "data science makes data powerful and data is everywhere"

character_count={}
characters=sentenc.split()
for item in characters:
    if item in character_count:
        character_count[item]+=1
    else:
        character_count[item]=1
print(character_count)














# same logic but question differant

string= "apple mango apple orange mango apple banana"
wor_count={}
wors=string.split()
for i in wors:
    if i in wor_count:
        wor_count[i]+=1
    else:
        wor_count[i]=1
        
most_frequent_word=max(wor_count,key=wor_count.get)
most_frequent_count=wor_count[most_frequent_word]
print("most frequent word is : ",most_frequent_word)
print("count : ",most_frequent_count)