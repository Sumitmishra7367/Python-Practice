# Q2. Word Lengths & Filter Long Words

Words=['data','science','is','fun','python']
length_of_words=list(map(lambda x:len(x),Words))
print(length_of_words)

result=list(filter(lambda x :x>=4,length_of_words))
print(result)

