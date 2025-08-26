# . एक list [10, 25, 30, 45, 50, 75, 100] से सिर्फ वो numbers निकालो जो 5 से divisible हों।

list_1=[10, 2, 30, 4, 50, 75, 100] 
result=list(filter(lambda x:x%5==0,list_1))
print(result)