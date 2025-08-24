
#print words in first character of vowels

item=['Anmol','Eva','Keshav']
vowels="AEIOUaeiou"
result_1=list(filter(lambda x : x[0] in vowels, item))
print(result_1)

list_1=['Anmol','Eva','Keshav']
vowel="AEIOUaeiou"
result=list(filter(lambda x: x[0] in vowels,list_1))

print(result)