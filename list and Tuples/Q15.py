#print maximum element withou using max function
list_1=[1,2,3,4,5,6,7,8,9,10,11]
maximum_elemnt=list_1[0]
for num in list_1:
    if num>maximum_elemnt:
        maximum_elemnt=num
print("The maximum element is : ",maximum_elemnt)



#print using max function
list_2=[22,11,33,44,55,77,66,99,88]
maximum=max(list_2)
print("the maximum element is : ",maximum)

#using another method
list_3=[22,11,33,44,55,77,66,99,88]
maximu=(sorted(set(list_3)))[-1]
print("The maximum element is : ",maximu)