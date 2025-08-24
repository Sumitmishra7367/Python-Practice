


text = "ai is future and ai is transforming the world with ai and data"

freq_words={}
for word in text.split():
    if word in freq_words:
        freq_words[word]+=1
    else:
        freq_words[word]=1
print("The most frequent words is ",freq_words)

top1_word=""
top1_count=0
top2_word=""
top2_count=0
for word,count in freq_words.items():
    if count>top1_count:
        top2_word,top2_count=top1_word,top1_count
        top1_word,top1_count=word,count
    elif count>top2_count:
        top2_word,top2_count=word,count
print("Top 1 word is ",top1_word, "count" ,top1_count)
print("Top 2 word is ",top2_word,"count",top2_count)