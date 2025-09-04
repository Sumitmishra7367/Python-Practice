
class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def display(self):
        print(f"Car _Name => {self.name} \nColor => {self.color}")


obj_1=Car("BMW","Black")
obj_2=Car("Audi","White")
obj_3=Car("Fortuner","Gray")
obj_1.display()
obj_2.display()
obj_3.display()
