# Fahrenheit → Celsius Conversion

def f_to_c(f):
    c=(f-32)*5/9                #Formula of fahrenhiet to celcius coversion : C=(F−32)×5/9
    return c
list_1=[32, 212, 98.6, 77]
result=list(map(f_to_c,list_1))
print(result)



# using lambda function

list_2=[32,212,98.6,77]
resul=list(map(lambda f:(f-32)*5/9,list_2))
print(resul)

