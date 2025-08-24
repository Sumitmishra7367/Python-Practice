# . Given a nested list (a list containing sublists), create a single flat list
nested_list=[[1,2],[3,4],[5,6],[7,8]]
flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)




nested_list_1=[[1,2],[3,4],[5,6],[7,8],[9,10]]
flat_list_1=[numbers for sublist_1 in nested_list_1 for numbers in sublist_1]
print(flat_list_1)