# number is prime or not
num=int(input("Enter the number : "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number ")
            break
    else:
        print(num,"is a prime number ")
else:
    print(num,"is not a prime number")








num_2=int(input("Enter the number : "))
if num_2>1:
    for i in range (2,num_2):
        if num%i==0:
            print(num_2,"is not a prime number ")
            break
    else:
        print(num_2,"is a prime number ")
else:
    print(num_2,"is not a prime number")





