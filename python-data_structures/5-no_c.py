#!/usr/bin/python3


def no_c(my_string):
    my_list = list(my_string)
    i = 0
    while i < len(my_list):
        if my_list[i] in "cC":
            del my_list[i]
        else:
            i += 1
    return "".join(my_list)

print(no_c("Charles"))
