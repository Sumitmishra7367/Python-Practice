# . list [2,3,4,5,6,7,8,9,10,11,13] में से सिर्फ prime numbers निकालो।

list_1=[2,3,4,5,6,7,8,9,10,11,13]

result=list(filter(lambda x:all(x % i !=0 for i in range(2,x)),list_1))

print(result)
