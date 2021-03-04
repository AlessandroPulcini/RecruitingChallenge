from Utils import InvalidOperationException


# Task 8
class Rectangle:
    def __init__(self, initb, inith):
        self.b = initb
        self.h = inith

    def area(self):
        return self.b * self.h


from math import pi


class Circle:
    def __init__(self, initr):
        self.r = initr

    def area(self):
        return self.r * self.r * pi


# Task 9
class Product:
    def __init__(self, initn, initp):
        self.name = initn
        self.price = initp

    def __str__(self):
        return self.name + " costs " + str(self.price) + " euro(s)"


# Task 10
class PhoneBook:
    def __init__(self):
        self.records = {}

    def add_number(self, name, number):
        """
       Add a contact or throw InvalidOperationException if it is already present
        :param number: an integer number
        :param name: a string
       """
        if name not in self.records:
            self.records[name] = number
        else:
            raise InvalidOperationException(AssertionError)

    def del_number(self, name):
        """
        Delete a contact or throw InvalidOperationException if it is not present
        :param name: a string
        """
        if name in self.records:
            del self.records[name]
        else:
            raise InvalidOperationException(AssertionError)

    def size(self):
        """
        :return: current size of PhoneBook
        """
        return len(self.records)

    def get_all(self):
        """
        return: a string representation of all entries in the format 'name: number',
        merged and separated by ';' and a space. The entries should be sorted alphabetically
        """
        output = ""
        keys_list = sorted(list(self.records.keys()))
        for key in keys_list:
            output += key + ": " + str(self.records[key]) + "; "
        return output[:-2]
