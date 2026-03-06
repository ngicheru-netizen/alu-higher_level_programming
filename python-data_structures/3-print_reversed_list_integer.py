#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    list = my_list
    for i in range(my_list):
        if isinstance(my_list[i], int):
            print.reverse("{:d}".format(my_list[i]))
        else:
            print("{}".format(my_list[i]))
