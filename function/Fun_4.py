#print sum of all digit from input user using without sum function
def sum(num):
    sum_digit=0
    for i in num:
        sum_digit+=int(i)
    return sum_digit
num=input("Enter the digits : ")
result=sum(num)
print("The sum of all digits : ",result)
