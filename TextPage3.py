def sort_array(source_array):
    odds = sorted((x for x in source_array if x % 2 == 1), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]


print(sort_array([5, 1, 2, 8, 3, 4]))
