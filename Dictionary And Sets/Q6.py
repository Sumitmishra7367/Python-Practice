# Har number ki frequency dictionary me store karo.


numbers = [4, 7, 2, 9, 4, 7, 4]
freq={}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)