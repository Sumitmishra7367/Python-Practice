# wheather all the digit of the number divide its or not
#mujhe is question ki practice karni hai


def all_digits_divide_number(n):
    original = n
    while n > 0:
        digit = n % 10
        if digit == 0 or original % digit != 0:
            return False
        n //= 10
    return True

# Example usage
number = 124
if all_digits_divide_number(number):
    print(f"Yes, all digits of {number} divide it.")
else:
    print(f"No, not all digits of {number} divide it.")

print(1//10)
