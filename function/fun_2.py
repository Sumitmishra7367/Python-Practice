#print maximum element without using max function but using function
def maximum(list_1):
    maximum_element=list_1[0]
    for i in list_1:
        if i >maximum_element:
            maximum_element=i
    return maximum_element
list_1=[1,2,3,4,5,66,7,8,99,10,11]
result=maximum(list_1)
print("The maximum element is : ",result)



