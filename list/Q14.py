#the sum of all integers number

list_6=[1,2,35,"sumit",True,5.1,7.6,45,1.6,55,36,99]
total=0
for num in list_6:
    if type(num)==int:
        total+=num
print("the sum of integers are : ",total)



#the sum of all float number
list_1=[1,2,35,"sumit",True,5.1,7.6,45,1.6,55,36,99,3.6,6.4,1.9]
total=0
for i in list_1:
    if type(i)==float:
        total+=i
print("The sum of float number is : ",total)


#the sum of all integers and floating numbers

data=[1,2,35,"sumit",True,5.1,7.6,45,1.6,55,36,99,3.6,6.4,1.9,22,41,20,22,41]
int_total=0
float_total=0
for numbers in data:
    if type(numbers) ==int:
        int_total+=numbers
    elif type(numbers)==float:
        float_total+=numbers
print("The sum of integers are :",int_total)
print("The sum of float numbers are: ",float_total)