# compare two list with their memory object and value
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a
print(a==b) #compare by value
print(c==a)
print(a is b)#compare by memory location
print(c is a)



list_1=[1,2,3,4,5]
list_2=[1,2,3,4,5]
list_3=list_1
print(list_1==list_2)
print(list_3==list_1)

print(list_1 is list_2)
print(list_1 is list_3)