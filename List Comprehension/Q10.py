# wheather all the digit of the number divide its or not
def all_digit_divide_number(n):
    original=n
    while n>0:
        digit=n%10
        if digit ==0 or original % digit!=0:
            return False
        n//10
        return True
    
number=int(input("Enter The number : "))
if all_digit_divide_number(number):
    print(f"yes, all digits of {number} divide it")
else:
    print(f"No, all digits of {number} divide it")

print(number)
