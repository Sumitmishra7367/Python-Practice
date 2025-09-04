class Person:
    name="sumit mishra"
    occupation="data analyst"
   

    def info(self):
        print(f"{self.name} is an {self.occupation}")

a=Person()  
b=Person()     #a is object
a.name="shubham"
a.occupation="Accountant"
b.name="Nitika"
b.occupation="HR"

a.info()
b.info()

