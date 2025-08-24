# . Given a nested list (a list containing sublists), create a single flat list

nested_list=[[1,2],[3,4],[5,6],[7,8]]
flat_list=[numbers for sublist in nested_list for numbers in sublist]
print(flat_list)

nested_list_1=[[1,2],[3,4],[5,6],[7,8],[9,10]]
flt_list=[num for sublist_1 in nested_list_1 for num in sublist_1]
print(flt_list)






nested_list_2=[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
main_list=[item for sublist_3 in nested_list_2 for item in sublist_3]
print("The main list of ",main_list)