#find even elements in a list
numbers=[10,11,12,13,14,15,16,17,18,19,20,21,22,223,24,255,26]
even_numbers=[]
for i in numbers :
    if i % 2==0:
       even_numbers.append(i)
print("the even number is : ",even_numbers)