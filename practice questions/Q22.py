#print odd numbers

for i in range(1, 11):  
    if i % 2 != 0:      
        print(i)

for num in range(1,15):
    if num %2 !=0:
        print(num)
 
 # list ke example se samjhte hai
list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
odd_number=[]
for item in list_1:
    if item %2 !=0:
        odd_number.append(item)
print("The odd number are : ",odd_number)