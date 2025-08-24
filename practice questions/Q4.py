#Q4. take input from user : name, age , country and give output that person is eligible for vote or not

name=input("Enter the name : ")
age = int(input("Enter the age : "))
country=input("Enter the country : ")

if age>=18:
    print(f"{name} from {country} is eligible to vote ")
else:
    print(f"{name} from {country} is not eligible to vote")








name=input("Enter the name : ")
age=int(input("enter the age : "))
country=input("Enter the country : ")
if age>=18:
    print(f"{name} from {country} is eligible to vote")
else:
    print(f"{name} from {country} is not eligible to vote")
    
