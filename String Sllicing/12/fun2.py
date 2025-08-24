#print even and odd numbers to given list
def even_odd_list(list_1):
    even_count=[]
    odd_count=[]
    for num in list_1:
        if num%2==0:
            even_count.append(num)
        else:
            odd_count.append(num)
    return even_count,odd_count
list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even,odd=even_odd_list(list_1)
print("even number : ",even)
print("odd numbers : ",odd)

list_2=[1,2,3,4,5,6,7,8]
maximum=max(list_2)
print("maximum",maximum)


list_3

