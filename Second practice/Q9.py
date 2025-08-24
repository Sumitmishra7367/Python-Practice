# make calculator,take two number from user and choice of operator and give respective output
num_1=int(input("Enter the number 1 : "))
num_2=int(input("Enter the number 2 : "))
operator=input("Enter the operator : ")
if operator=="+":
    result=num_1+num_2
    print(result)
elif operator =="-":
    result=num_1-num_2
    print(result)
elif operator=="*":
    result=num_1*num_2
    print(result)
elif operator=="/":
    result=num_1/num_2
    print(result)
elif operator =="**":
    result=num_1**num_2
    print(result)
elif operator=="//":
    result=num_1//num_2
    print(result)