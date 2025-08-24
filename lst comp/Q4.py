## Merge Two Sorted list in single list
#mujhe is question ki prctice karni h

def merged_list(list_1, list_2):
    result_list = []

    i=j=0
    while i < len(list_1) and j < len(list_2):
        if list_1[i]<list_2[j]:
            result_list.append(list_1[i])
            i+=1
        else:
            result_list.append(list_2[j])
            j+=1

    result_list.extend(list_1[i:])
    result_list.extend(list_2[j:])

    return result_list

list_1 =[1,3,5,7,9,11,13]
list_2 = [2,4,6,8]

result=merged_list(list_1, list_2)
print(result)



