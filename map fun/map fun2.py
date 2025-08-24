#print sqaures of numbers in the list using map and lambda fun. 
 
list_1=[1,2,3,4,5]
squared_list=list(map(lambda x:x**2,list_1))
print(squared_list)

#print square of number without lambda fun. but using map  fun.
def squard_list(x):
    return x**2
list_2=[1,2,3,4,5,6,7]
result=list(map(squard_list,list_2))
print(result)


# given list print uppercase of each string
def upper_case(x):
    return x.upper()
list_3=["sumit","mishra","golu","aditya"]
result=list(map(upper_case,list_3))
print(result)

#print first charcter of each string
def first_char(y):
    return y[0]  #access first element of each string
list_4=["sumit","mishra","golu","aditya"]
result=list(map(first_char,list_4))
print(result)

