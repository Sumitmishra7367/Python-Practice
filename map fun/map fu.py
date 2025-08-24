list_0=[1,2,3,4,5]
squared_list=list(map(lambda x:x**2,list_0))
print(squared_list)

def square_list(x):
    return x **2
list_1 = [1,2,3,4,5]
result=list(map(square_list,list_1))
print(result)



def upper_case(x):
    return x.upper()
list_2 = ["ram", "sham", "apple"]
result_1=list(map(upper_case,list_2))
print(result_1)



def first_letter(x):
    return x[0]
list_3=["Sumit","Komal","vishal"]
result_2=list(map(first_letter,list_3))
print(result_2)



def length(x):
    return len(x)
list_4=["Sumit","Komal","vishal"]
result_3=list(map(length,list_4))
print(result_3)
