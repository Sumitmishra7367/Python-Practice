#print even numbers and odd numbers to given list and using functions
def even_odd_list(list_1):
    even_list=[]
    odd_list=[]
    for num in list_1:
        if num%2==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list,odd_list
list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even,odd=even_odd_list(list_1) #calling function
print("The even number is : ",even)
print("The odd number is : ",odd)