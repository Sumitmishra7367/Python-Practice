with open("sample.txt",'a') as f:    #appending into file 
    f.write("\ni am graduated from Chandigarh University")


with  open("content.txt",'a')as f:   #creating file and write a file
    f.write("\n My name is sumit mishra ")

with open("Content.txt",'r')as f:  #reading a file
    abc=f.read()
    print(abc)

    with open("file.txt",'w')as f:
        f.write("Hello my name is sumit mishra")
       
    with open("file.txt",'a')as f:
        f.write("\nThis is a python file" )

    with open("file.txt",'r')as f:
        ab=f.read()
        print(ab)
