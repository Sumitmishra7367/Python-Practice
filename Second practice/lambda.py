x=lambda a,b:a+b
print(x(1,3))

y=lambda a,b:a-b
print(y(5,2))


print((lambda a,b,c:a+b+c)(4,5,6))

print((lambda x,y,z:x*y*z)(4,5,6))


double=lambda x: x*2
print(double(5))

cube=lambda x:x*x*x
print(cube(5))


average=lambda x,y:(x+y)//2
print(average(3,5))

avg=lambda x,y,z:(x+y+z)/2
print(avg(4,5,6))



def fun(a,b):
    return a*b
call=fun(4,5)
print(call)


