# . Given a list of numbers, create a new list containing the squares of only the even numbers.


list_1=[1,2,3,4,5,6,7,8,9,10,11,12]
square=[num**2 if num%2==0 else num for num in list_1]
print(square)



# same question in odd numbers 
list_2=[1,2,3,4,5,6,7,8,9,10,11,12]
odd_square=[i**2 if i%2!=0 else i for i in list_2]
print(odd_square)
