# print length of even numbers
list_1=[10,11,12,13,14,15,16,17,18,19,21,20,22,23]
length=0
for i in list_1:
    if i %2==0:
        length+=1
print("The length of even number is : ",length)