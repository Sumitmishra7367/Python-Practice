# सभी even numbers निकालो (list comprehension और filter दोनों से)।
# फिर उनका square निकालो (map या list comprehension से)।

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_number=[x for x in nums if x %2==0]  #using list comprehension
print(even_number)

num= [1, 2, 3, 4, 5, 6, 7, 8, 9]
result=list(filter(lambda x:x%2==0,num))   #using filter fun.
print(result)


list_1= [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num=list(filter(lambda x:x%2==0,list_1))
result=list(map(lambda x:x**2,even_num))
print(result)