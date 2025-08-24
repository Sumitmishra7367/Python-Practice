#compare two list with their memory object and value

a=[1,2,3,4]
b=[1,2,3,4]
c=a
print(a==b)
print(c==a)
print(a is b)
print(c is a)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # Points to same object as list1

# Compare by value
print(list1 == list2)  # True (contents are same)
print(list1 == list3)  # True (contents are same)

# Compare by memory location
print(list1 is list2)  # False (different objects in memory)
print(list1 is list3)  # True (same object in memory)










num_1=[1,2,3,4,5]
num_2=[1,2,3,4,5]
print(num_1==num_2) # kyuki value same hai to ye opreator compare karne pe true batayega

num_3=[3,4,5,6]
num_4=[1,2,4,5]
print(num_3==num_4) # kyuki value alag h to false batayega


num_5=[1,2,3,4,5,6]
num_6=[1,2,3,4,5,6]
num_7=num_5
print(num_5 is  num_6) #because dono list ki value ki memory location alag hai to  false batayega
print(num_7 is  num_5) #iski same hai to true batayega
