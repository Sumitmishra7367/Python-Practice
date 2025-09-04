#area of triangle

class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area_of_triangle(self):
        print(f"The area of triangle is {1/2*self.base*self.height}")
    
base=int(input("Enter the Base : "))
height=int(input("Enter the Height: "))

obj=Triangle(base,height)
obj.area_of_triangle()
