




text = "python programming is fun and python programming is powerful and python"


freq_word={}
for item in text.split():
    if item in freq_word:
        freq_word[item]+=1
    else:
        freq_word[item]=1
print("The most frequntly word is : ",freq_word)

top1_word=""
top1_count=0
top2_word=""
top2_count=0

for word,count in freq_word.items():
    if count>top1_count:
        top2_word,top2_count=top1_word,top1_count
        top1_word,top1_count=word,count
    elif count>top2_count:
        top2_word,top2_count=word,count

print("The top 1 word is : ",top1_word,"count :",top1_count)
print("top 2 word is : ",top2_word, "count : ",top2_count )