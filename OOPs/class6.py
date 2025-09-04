class Car:
    def __init__(self,name,color,speed,engine):
        self.name=name
        self.color=color
        self.speed=speed
        self.engine=engine
    
    def display(self):
        print(f"Car_Name {self.name}\ncolor=>{self.color}\nspeed=> {self.speed}\nengine=> {self.engine}")


obj=Car("Audi","black","120","Powerful")
obj.display()

