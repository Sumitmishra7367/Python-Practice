from functools import reduce

number=98765
digits=[int(d) for d in str(number)]
result=reduce(lambda x,y:x+y ,digits)

print(result)