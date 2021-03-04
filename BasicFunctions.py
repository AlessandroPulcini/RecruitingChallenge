# Task 1
from typing import List, Any


def average(a, b):
    return (a + b) / 2


# Task 2
def reverse_list(input_list):
    return input_list[::-1]


# Task 3
def sort_numbers_descending(number_list):
    return sorted(number_list, reverse=True)


# Task 4
def add_indices(string_list):
    for index, element in enumerate(string_list):
        string_list[index] = str(index + 1) + ". " + element
    return string_list


# Task 5
def capitalize_last_letter_in_each_word(string):
    new_string = ""
    for word in string.split():
        new_string += word[:-1] + word[-1].upper() + " "
    return new_string[:-1]


# Task 6
def element_wise_merge(list1, list2):
    """
    Function that performs element-wise merge of list elements, inserting blank space in between
    :param list1: list of string
    :param list2: list of strings of the same length as list1
    :return: new list of merged strings
    """
    merged_list = []
    for el1, el2 in zip(list1, list2):
        new_element = el1 + " " + el2
        merged_list.append(new_element)
    return merged_list


# Task 7
def execute_safely(operator, a, b):
    """
    Function that executes operator on arguments (a, b) -- or returns -1
    :param operator: some real-valued function, taking on input two real arguments
    :param a: a real number
    :param b: a real number
    :return: operator evaluated on (a,b) -- or -1 if this operation would be illegal
    """
    try:
        result = operator(a, b)
    except (ZeroDivisionError, ValueError):
        result=-1
    return result
