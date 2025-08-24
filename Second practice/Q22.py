# print odd numbers

# for i in range(1,10):
#     if i%2!=0:
#         print(i,end=" ")


# for num in range(1,20):
#     if num%2!=0:
#         print(num,end=" ")


list_1=[11,22,33,44,55,66,77,88,99,111]
odd_list=[]
for item in list_1:
    if item !=0:
        odd_list.append(item)
print("The odd numbers are : ",odd_list)