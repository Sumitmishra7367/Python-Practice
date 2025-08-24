#print sum sbtract and multiplicaton to given condition and using function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

num_1=int(input("Enter the number 1 :"))
num_2=int(input("Enter the number 2 :"))
if num_1>num_2:
    result=sub(num_1,num_2)
    print("result :",result)
elif num_1<num_2:
    result=add(num_1,num_2)
    print("result : ",result)
elif num_1==num_2:
    result=mul(num_1,num_2)
    print("Result : ",result)