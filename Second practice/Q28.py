# print  the length of upper and lowercase
str_1="Hello Sumit Mishra"
upper_count=0
lower_count=0
for i in str_1:
    if i.isupper():     #isupper use krte h uppercase find ya check krne ke liye
        upper_count+=1
    elif i.islower(): #islowerr use krte h lowercase find ya check krne ke liye
        lower_count+=1
print("The count of upper letter are : ",upper_count)
print("The count of lower letter are : ",lower_count)