#extract even and odd list from main list
numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
even_number=[]
odd_numbers=[]
for num in numbers:
    if num %2==0:
        even_number.append(num)
    elif num%2!=0:
        odd_numbers.append(num)
print("even list : ",even_number)
print("odd list : ",odd_numbers)