#find median

list_1=[2,4,1,7,5,3,9,8,6,10]
list_1.sort()
length=len(list_1)
median=(list_1[length//2]+list_1[length//2-1])/2
print(median)

