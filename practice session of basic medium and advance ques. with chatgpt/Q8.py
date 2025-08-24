# Har fruit ki frequency dictionary me store karo

# Fir print karo fruit jo sabse zyada baar aaya hai aur uska count alag variables me


fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "mango"]
fruits_count={}
for item in fruits:
    if item in fruits_count:
        fruits_count[item]+=1
    else:
        fruits_count[item]=1

max_fruit_word=max(fruits_count,key=fruits_count.get)
max_fruit_count=fruits_count[max_fruit_word]
print("The maximum fruit is ",max_fruit_word)
print("count" ,max_fruit_count)









string= "apple mango apple orange mango apple banana"
word_count={}
for item in string.split():
    if item in word_count:
        word_count[item]+=1
    else:
        word_count[item]=1
max_word_repeat=max(word_count,key=word_count.get)
max_word_count=word_count[max_word_repeat]
print("The maximum Fruit repeat is : ",max_word_repeat)
print("count : " ,max_word_count  )





