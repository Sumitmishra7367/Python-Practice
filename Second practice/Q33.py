str_1="$i#am$a$boy@"
replace=""
for i in str_1:
    if not i.isalnum():
        replace+=" "
    else:
        replace+=i
print("original string " ,str_1)
print("replaced string :",replace)



