# list ["madam", "hello", "level", "python", "radar"] में से सिर्फ palindrome words निकालो।

list_1=["madam", "hello", "level", "python", "radar"]


result=list(filter(lambda x:x==x[: : -1],list_1))
print(result)



list_2=["madam", "hello", "level", "python", "radar"]

resu=list(filter(lambda x:x==x[: :-1],list_2))
print(resu)
