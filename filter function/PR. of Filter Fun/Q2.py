# एक string list ["hi", "python", "world", "ai", "filter"] से सिर्फ वो words filter करो जिनकी length > 3 है।


list_2=["hi", "python", "world", "ai", "filter"]
result=list(filter(lambda x:len(x)>3,list_2))
print(result)