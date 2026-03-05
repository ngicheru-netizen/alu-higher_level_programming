#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None


my_list = [1, 2, 3, 4, 5]
idx = 45
my_list[3] = 7
element = 32
result = replace_in_list(my_list, idx, element)
replace_in_list(my_list, idx, element)
