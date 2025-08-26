# Q5: List me tuple hai (name, marks), marks ko 10% increase karo aur naya tuple return karo.

students = [('Alice', 80), ('Bob', 90), ('Charlie', 70)]

result=list(map(lambda x:(x[0],x[1]*1.1),students))
print(result)
