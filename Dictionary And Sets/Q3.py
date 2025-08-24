# print all keys and all values aur dono ek sath key value pair me


student = {"name": "Sumit", "age": 21, "marks": 85}

print(student.keys())
print(student.values())
print(student.items())

#line by line print karana ho to

for key,value in student.items():
    print(key, " : ",value)