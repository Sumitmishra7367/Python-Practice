from functools import reduce

#Find longest word

words = ["python", "reduce", "function", "programming", "ai"]
result=reduce(lambda x,y:x if len(x)>len(y) else y,words )
print("Longest Word : ",result)


#Find Shortest Word

Word=["python", "reduce", "function", "programming", "ai"]
resu=reduce(lambda x,y :x if len(x)<len(y) else y,Word)
print("Shortes Word : ",resu)