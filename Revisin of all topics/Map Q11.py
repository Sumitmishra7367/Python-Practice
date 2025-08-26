#  List of strings me check karo kaun palindrome hai aur ek boolean list return karo

words = ['level', 'python', 'radar', 'data']

result=list(map(lambda x:x==x[: :-1],words))
print(result)