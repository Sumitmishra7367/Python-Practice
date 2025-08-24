# Har word ka frequency nikalna hai
# Fir print karna hai 2 words jo sabse zyada baar aaye hain aur unka count

text = "data science is fun and data is everywhere in data science"
word_count={}
for item in text.split():
    if item in word_count:
        word_count[item]+=1
    else:
        word_count[item]=1
print("word frequncy dictionary : ",word_count)

top1_word=""
top1_count=0
top2_word=""
top2_count=0
for item,count in word_count.items():
    if count>top1_count:
        top2_word,top2_count=top1_word,top1_count
        top1_word,top1_count=item,count
    elif count>top2_count:
        top2_word,top2_count=item,count

print("Top two most frequent word is ")
print("Top 1 word :  ",top1_word ,"count : ",top1_count)

print("Top 2 word :  ",top2_word ,"count : ",top2_count)