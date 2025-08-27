# Python program to create a simple calculator

# Three steps to build calculator program
#       1. Function for operations
#       2. User input 
#       3. Print result


# Step -1: Create Function

#Function to add two numbers
def add(num_1,num_2):
    return num_1+num_2

#Function to Subtract two numbers
def sub(num_1,num_2):
    return num_1-num_2

#Function to Multiplication two numbers
def multiply(num_1,num_2):
    return num_1*num_2

#Function to division two numbers
def divide(num_1,num_2):
    return num_1/num_2

#Function to average two numbers
def avg(num_1,num_2):
    return (num_1+num_2)/2

#Function to Floar division two numbers
def floor(num_1,num_2):
    return num_1//num_2


#Step-2: User input
print("\n========= Simple Calculator =========")
print("Please Select a operations :\n" 
 "\n 1.Addition" "\n 2.Subtraction" "\n 3.Multiplication" "\n 4.Division ""\n 5.Average" "\n 6.Floor Division")

print("=====================================")

select=int(input("Selct a operation from 1,2,3,4,5,6 : "))
number_1=int(input("Enter the num_1 : "))
number_2=int(input("Enter the num_2 : "))


#Step-3 : Print result

if select ==1:
    print(number_1, "+" , number_2, "=",add(number_1,number_2))
elif select==2:
    print(number_1,"-",number_2,"=",sub(number_1,number_2))
elif select==3:
    print(number_1,"*",number_2,"=",multiply(number_1,number_2))
elif select==4:
    print(number_1,"/",number_2,"=",divide(number_1,number_2))
elif select==5:
    print("(",number_1,"+",number_2,")","/","2","=",avg(number_1,number_2))
elif select==6:
    print(number_1,"//",number_2,"=",floor(number_1,number_2))
else:
    print("invalid operation Please select again")


