# taking input from the user print all the odd number upto that input number
numbers=int(input("Enter the number : "))
for num in range(1,numbers+1):

    if num%2!=0:
        print(num ,end=" ")



n = int(input("Enter a number: "))

i=1
while i<=n:
    if i %2!=0:
        print(i, end =" ")
    i+=1