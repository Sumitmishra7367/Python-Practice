
def lower(str_1):
    str_2=""
    for i in str_1:
        if i.isupper():
            str_2+=i
        elif i.islower():
            str_2+=i
    return str_2
str_1="ApPlE"
reult=lower(str_1)
print(reult)