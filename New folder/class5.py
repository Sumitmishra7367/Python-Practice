# Q1.find area of square

class Square:
    def __init__(self,side):
        self.side=side
    
    def area_of_square(self):
        return self.side**2

side=int(input("Enter the length : "))
obj=Square(side)
print(f"The area of square is {obj.area_of_square()}")