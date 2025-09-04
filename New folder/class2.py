# Sum of two number using class

class Abc:
    def add(a,b):
        print(f"sum=>{a+b}")
    def sub(a,b):
        print(f"sub=>{a-b}")


a=int(input("enter the number a : "))
b=int(input("Enter the number b : "))
operator =input("Enter the operator : ")

obj=Abc
obj.add(a,b)
obj.sub(a,b)


""