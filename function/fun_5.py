#count even numbers and odd numbers to given list and using functions
def even_odd_count(list_1):
    even_count=0
    odd_count=0
    for num in list_1:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count
list_1=[11,22,33,44,55,66,77,88,99,110,111]
result1,result2=even_odd_count(list_1)
print("the count of even number is",result1)
print("the count of odd number is ",result2)