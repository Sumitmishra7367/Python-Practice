#number of sqaure

class Square:
    def __init__(self,no_of_square):
        self.no_of_square=no_of_square

    def square_of_numbers(self):
        print(f"The number of square => {self.no_of_square**2}")

number=int(input("Enter the number : "))
obj=Square(number)
obj.square_of_numbers()
    