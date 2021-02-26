# Task 1
def average(a, b):
    average = (a + b) / 2
    return average


# Task 2
def reverse_list(input_list):
    return input_list[::-1]


# Task 3
def sort_numbers_descending(number_list):
    reverse_order_list = number_list[:]
    reverse_order_list.sort(reverse=True)
    return reverse_order_list


# Task 4
def add_indices(string_list):
    return None


# Task 5
def capitalize_last_letter_in_each_word(string):
    return None


# Task 6
def element_wise_merge(list1, list2):
    """
    Function that performs element-wise merge of list elements, inserting blank space in between
    :param list1: list of string
    :param list2: list of strings of the same length as list1
    :return: new list of merged strings
    """
    return None


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
    except ZeroDivisionError:
        result=-1
    except ValueError:
        result=-1
    return result
