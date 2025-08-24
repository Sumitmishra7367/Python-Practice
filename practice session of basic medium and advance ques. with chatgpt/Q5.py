# hume nikalna hai har character ki frequency dictionary me.

text = "hello world"
freq={}
for char in text  :
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)




# Same logic but question differnt
str_1 = "datascience"
freq_1={}
for j in str_1:
    if j in freq_1:
        freq_1[j]+=1
    else:
        freq_1[j]=1
print(freq_1)







# Same logic but question differnt
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
count_fruits={}
for i in fruits:
    if i in count_fruits:
        count_fruits[i]+=1
    else:
        count_fruits[i]=1
print(count_fruits)
