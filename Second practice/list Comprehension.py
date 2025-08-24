# . Given a list of numbers, create a new list containing the squares of only the even numbers.
numbers=[1,2,3,4,5,6,7,8,9,10,11]
square=[i**2 if i %2==0 else i for i in numbers]
print(square)



list_1=[1,2,3,4,5,6,7,8,9,10]
result=["odd" if num %2!=0 else num for num in list_1 ]
print(result)




list_2=[1,2,3,4,5,6,7,8,9,70,11.12]
resul=["Even" if num%2==0 else num for num in list_2]
print(resul)


# using normal and another method
list_3=[1,2,3,4,5,6,7,8,9,70,11.12]
abc=[]
for i in list_3:
    if i%2==0:
        abc.append("EVEN")
    else:
        abc.append(i)
print(abc)
