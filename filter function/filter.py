#print only positve number using filter function
list_1=[-2,-1,0,1,2,3,4,5]
result=list(filter(lambda x:x>0,list_1)) 
print(result)

#print only even number using filter function

list_2=[1,2,3,4,5,6,7,8,9,10,11]
res=list(filter(lambda x:x%2==0,list_2))
print("The only even number is : ",res)


#print only odd number using filter function

list_3=[1,2,3,4,5,6,7,8,9,10,11]
r=list(filter(lambda x:x%2!=0,list_3))
print("odd numbers is ", r)


#print words in first character of vowels

item=['Anmol','Eva','Keshav']
vowels="AEIOUaeiou"
result_1=list(filter(lambda x : x[0] in vowels, item))
print(result_1)


