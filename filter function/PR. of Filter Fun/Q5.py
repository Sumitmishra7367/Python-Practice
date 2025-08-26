# . एक list [5, 10, 15, 20, 25, 30, 35] से सिर्फ 20 से बड़े numbers filter करो।


list_1=[5, 10, 15, 20, 25, 30, 35]

result=list(filter(lambda x :x>20,list_1))
print(result)