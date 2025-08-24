#print middle elemnt of each string

def middle_char(x):
    mid_index=(len(x))//2
    return x[mid_index]
list_1=["heleo","python","programming"]
result=list(map(middle_char,list_1))
print(result)





#second try

list_2=["heleo","python","programming"]


result=list(map(lambda x:x[len(x)//2],list_2))
print(result)


