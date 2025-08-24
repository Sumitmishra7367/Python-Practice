# find maximu and minimum

numbers = [5, 10, 15, 20, 25, 30]
maximum=numbers[0]
minimum=numbers[0]
for i in numbers:
    if i>maximum:
        maximum=i
    elif i<minimum:
        minimum=i
print("The maximum number is : ",maximum)
print ("The minimum no. is : ",minimum)


