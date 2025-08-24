# sum of all odd and even numbers numbers

list_3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,25,23,48,96,99,9,5]
even_total=0
odd_total=0
for num in list_3:
    if num%2==1:
       odd_total+=num
    else:
        even_total+=num
print("the sum of odd number is : ",odd_total )
print("The sum of even number is : ",even_total)