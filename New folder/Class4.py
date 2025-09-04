#find area of circle and circum of circle
class Circle:
    def __init__(self,radius,circum):
        self.radius=radius
        self.circum=circum

    def area_circle(self):
        print(f"area of circle is {3.14*self.radius**2}")
    
    def circum_of_circle(self):
        print(f"circum of circle {2*3.14*self.radius}")

radius=int(input("Enter the radius : "))
obj=Circle(radius,circum=radius)
obj.area_circle()
obj.circum_of_circle()
