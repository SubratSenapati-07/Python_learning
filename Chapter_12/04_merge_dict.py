dict1 = {'a': 10,'b' :20}
# dict2 = {'a': 2,'b': 4} [More priority]
dict2 = {'c': 2,'d': 4}
merge = dict1 | dict2 # | merge krta ha do dictonary ko
print(merge)  # Agar dict1 | dict2 {It means first priority dict2 ko milega}
