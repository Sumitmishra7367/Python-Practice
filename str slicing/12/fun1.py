def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
num_1=int(input("Enter the number 1 : "))
num_2=int(input("Enter the number 2 : "))
if num_1>num_2:
    result=add(num_1,num_2)
    print(result)
elif num_1<num_2:
    result=sub(num_1,num_2)
    print(result)

elif num_1==num_2:
    result=mul(num_1,num_1)
    print(result)

def vowel_count(str_1):
    vowels="AEIOUaeiou"
    count=0
    for i in str_1:
        if i in vowels:
            count+=1
    return count
str_1=input("Enter the string : ")
result=vowel_count(str_1)
print(result)

def replace(str_2):
    vowels="AEIOUaeiou"
    result=""
    for char in str_2:
        if char in vowels:
            result+="$"
        else:
            result+=char
    return result
str_2=input("Enter the string : ")
abc=replace(str_2)
print(abc)


def repl(str_3):
    result=""
    for i in str_3:
        if not i.isalnum():
            result+=" "
        else:
            result+=i
    return result
str_3='i$am@a!boy!'
abc=repl(str_3)
print(abc)