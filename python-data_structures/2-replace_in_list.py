#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None


my_list = [1, 2, 3]
idx = 1
new_element = 4
result = replace_in_list(my_list, idx, new_element)
replace_in_list(my_list, idx, new_element)
print(result)
print(my_list)
