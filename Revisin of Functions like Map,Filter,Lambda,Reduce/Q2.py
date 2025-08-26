# हर character की frequency निकालो dictionary में।
# सिर्फ वो characters print करो जिनकी frequency > 1 है।

string="data science with python"
freq={}
for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1  
# print(freq)              हर character की frequency निकालो dictionary में।

for key,values in freq.items():       #print frequency>1
    if values>1:
        print(f"{key} :{values}",end=" ")








str_2="data science with python"
frequency={}
for item in str_2:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)

for keys,values in frequency.items():
    if values>1:
        print(f"{keys}: {values}")
        