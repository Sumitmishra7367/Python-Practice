#find length of list of each string

def len_str(x):
    length=0
    for i in x:
        length+=1
    return length
list_1=['sumit','kamlesh','keshav']
Result=list(map(len_str,list_1))
print(Result)




list_3=['sumit','kamlesh','keshav']

Result=list(map(lambda x: len(x) ,list_3))
print(Result)


