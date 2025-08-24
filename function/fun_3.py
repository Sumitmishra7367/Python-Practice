#print minimum element without using min function but using function
def minimum(list_1):
    minimum_element=list_1[0]
    for i in list_1:
        if i<minimum_element:
            minimum_element=i
    return minimum_element
list_1=[2,1,3,45,6,4,5,]
result=minimum(list_1)
print("The minimum element is : ",result)