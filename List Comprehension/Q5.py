# count duplicate character in string
str_1=input("Enter the string : ")
duplicate={}
duplicate_count=0

for i in str_1:
    if i in duplicate:
        duplicate[i]+=1
    else:
        duplicate[i]=1
for j in duplicate.values():
    if j>1:
       duplicate_count+=1

print("Duplicates values =",duplicate_count)


