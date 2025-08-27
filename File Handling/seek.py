# with open("seek.txt",'w')as f:
#     f.write("My name is sumit mishra ")


with open ("seek.txt",'r')as f:
    abc=f.read()
    print(abc)



f=open("seek.txt",'r')
f.seek(7) 
print(f.readlines())  
 



