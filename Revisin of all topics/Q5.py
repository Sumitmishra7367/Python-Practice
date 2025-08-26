# List flattening:
# data = [[1, 2], [3, 4], [5, 6, 7]]

# Output चाहिए: [1, 2, 3, 4, 5, 6, 7]
# (list comprehension या itertools का use करके)।

data = [[1, 2], [3, 4], [5, 6, 7]]
result=[item for sublist in data for item in sublist]
print(result)



