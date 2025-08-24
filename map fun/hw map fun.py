#convert celcius to fahrenhiet

def c_to_f(c):
  return (c*9/5)+32
lis=[36.5,37.1,35.1]
result=list(map(c_to_f,lis))
print("Fahrenhiet :",result)







def c_to_f(s):
    c=float(s.rstrip("c"))
    fahren=(c*9/5)+32
    return f"{fahren:.2f}F" 
list_2=["36.5c","35.1c","37.1c"]
result=list(map(c_to_f,list_2))
print("Fahrenhiet : ",result)






def c_to_f (s):
   c=float(s.rstrip("c"))
   fahren=(c*9/5)+32
   return f"{fahren : .2f}F"
list_3=["36.5c","35.1c","37.1c"]
result=list(map(c_to_f,list_3))
print(result)