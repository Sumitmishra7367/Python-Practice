# . Count Vowels in Each Word

words=['data', 'science', 'python']
vowels="aeiouAEIOU"
count=0
result=list(map(lambda word:sum(1 for y in word if y in vowels ),words))
print(result)
