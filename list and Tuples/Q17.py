# find prime number

list_1=[2,3,4,5,6,7,8,9,10]
prime_numbers=[]
for num in list_1:
    if num>1:
        is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
            prime_numbers.append(num)
print(prime_numbers)






list_2=[2,3,4,5,6,7,8,9,10,11]
prime_number=[]
for num in list_2:
    if num>1:
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            prime_number.append(num)
print("prime numbers :",prime_number)
        
