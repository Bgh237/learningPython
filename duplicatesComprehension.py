#Show only the duplicates in the list using comprehension

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({value for value in some_list if some_list.count(value) > 1})

print(duplicates)