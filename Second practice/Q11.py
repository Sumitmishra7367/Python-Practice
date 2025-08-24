#find length of list
list_1=[10,20,30,40,50,60,70,80,90,100]
length=len(list_1)
print("The length of list is : ",length)

# Second method
list_2=[11,22,33,44,55,66,77,88,99]
length_1=0
for i in list_2:
    if i>=0:
        length_1+=1
print("The length of list is : ",length_1)