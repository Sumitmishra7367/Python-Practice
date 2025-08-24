# . Given a list of numbers, create a new list containing the squares of only the even numbers.

list_1=[1,2,3,4,5,6,7,8,9,10,11,12]
even_square=[i**2 if i %2==0 else i for i in list_1]
print(even_square)



#same odd numbers 

list_2=[1,2,3,4,5,6,7,8,9,10,11,12]
odd_square=[x**2 if x%2!=0 else x for x in list_2]
print(list_2)








list_3=[1,2,3,4,5,6,7,8,9,10,11,12]
square_even=[x**2 if x%2==0 else x for x in list_3]
print("The square of even numbers : ",square_even)
