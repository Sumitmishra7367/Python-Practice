# find second largest element in list
numbers=[10,20,30,80,50,60,70]
second_largest=sorted(set(numbers))[-2]
print("second largest number is : ",second_largest)


# set() removes duplicates.

# sorted() arranges in ascending order.

# [-2] picks the second last item.

num_1=[11,22,33,55,44,77,66,99,88]
second_largest=sorted(set(num_1))[-2]
print("the second largest number is : ",second_largest)